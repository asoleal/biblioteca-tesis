# generar_vault.py v2 — vault .md desde Zotero (grupo) + .bib maestro
import re, shutil, sqlite3, sys, tempfile
from pathlib import Path

VAULT = Path(sys.argv[1]) / 'vault'
HOME = Path.home()
BIB = HOME/'Zotero/Tesis_profesor_leal.bib'
REPOS = [HOME/'proyecto-tesis', Path('/mnt/Compartida/Descargas_HDD/tesis-doctorado/tesis-BSF')]

tmp = Path(tempfile.mkdtemp())
for f in (HOME/'Zotero').glob('zotero.sqlite*'): shutil.copy(f, tmp/f.name)
db = sqlite3.connect(tmp/'zotero.sqlite'); db.row_factory = sqlite3.Row

items = {}
for r in db.execute("""SELECT i.itemID, it.typeName FROM items i
  JOIN itemTypes it ON i.itemTypeID=it.itemTypeID
  JOIN libraries l ON i.libraryID=l.libraryID AND l.type='group'
  WHERE it.typeName NOT IN ('attachment','note')
  AND i.itemID NOT IN (SELECT itemID FROM deletedItems)"""):
    items[r['itemID']] = {'type': r['typeName'], 'autores': [], 'tags': []}

for r in db.execute("""SELECT d.itemID, f.fieldName, v.value FROM itemData d
  JOIN fields f ON d.fieldID=f.fieldID JOIN itemDataValues v ON d.valueID=v.valueID"""):
    if r['itemID'] in items: items[r['itemID']][r['fieldName']] = r['value']

nuevo = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='creatorData'").fetchone() is None
qc = ("""SELECT ic.itemID, c.lastName, c.firstName FROM itemCreators ic JOIN creators c ON ic.creatorID=c.creatorID ORDER BY ic.itemID, ic.orderIndex""" if nuevo
      else """SELECT ic.itemID, cd.lastName, cd.firstName FROM itemCreators ic JOIN creators c ON ic.creatorID=c.creatorID JOIN creatorData cd ON c.creatorDataID=cd.creatorDataID ORDER BY ic.itemID, ic.orderIndex""")
for r in db.execute(qc):
    if r['itemID'] in items:
        nom = (r['lastName'] or '') + (', ' + r['firstName'] if r['firstName'] else '')
        if nom.strip(): items[r['itemID']]['autores'].append(nom.strip(', '))

for r in db.execute("SELECT it.itemID, t.name FROM itemTags it JOIN tags t ON it.tagID=t.tagID"):
    if r['itemID'] in items: items[r['itemID']]['tags'].append(r['name'])

pdfs = set(r[0] for r in db.execute("SELECT parentItemID FROM itemAttachments WHERE contentType='application/pdf' AND parentItemID IS NOT NULL"))

def norm_doi(d): return re.sub(r'^https?://(dx\.)?doi\.org/', '', (d or '').lower().strip())
def norm_tit(t): return ' '.join(re.sub(r'[^a-z0-9 ]', ' ', (t or '').lower()).split())
bib = BIB.read_text(encoding='utf-8', errors='ignore')
bib_doi, bib_tit, bib_rec = {}, {}, {}
CAMPO = r'(\w+)\s*=\s*\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}'
for typ, key, body in re.findall(r'@(\w+)\{([^,]+),(.*?)\n\}', bib, re.S):
    f = dict(re.findall(CAMPO, body))
    bib_rec[key] = {'type': typ, **f}
    if f.get('doi'): bib_doi[norm_doi(f['doi'])] = key
    if f.get('title'): bib_tit.setdefault(norm_tit(f['title']), key)

usadas = {}
for repo in REPOS:
    if not repo.is_dir(): continue
    for tex in repo.rglob('*.tex'):
        if '.git' in tex.parts: continue
        for m in re.finditer(r'\\[a-zA-Z]*cite[a-zA-Z]*(?:\s*\[[^\]]*\])*\{([^}]+)\}', tex.read_text(encoding='utf-8', errors='ignore')):
            for k in m.group(1).split(','):
                k = k.strip()
                if k: usadas.setdefault(k, set()).add(f'{repo.name}/{tex.relative_to(tex.parts[0] and repo)}')

TEMAS = [
 ('01-bsf-gei', ['hermetia','black soldier','bsf'], ['emission','greenhouse','co2','ch4','methane','gei','gas']),
 ('02-bsf-modelado', ['hermetia','black soldier','bsf','insect'], ['model','growth','kinetic','dynamic','simulation','oxygen','consumption','assimilation','energy budget','bioprocess']),
 ('03-bsf-general', ['hermetia','black soldier','bsf'], []),
 ('05-iot-sensores', ['iot','internet of things','sensor','digital twin','gemelo','monitoring','wireless','smart'], []),
 ('06-ml-ia', ['machine learning','deep learning','neural','artificial intelligence','random forest','big data','prediction','optimization'], []),
 ('08-acv', ['life cycle','lca'], []),
 ('09-deb-bioenergetica', ['dynamic energy budget','metabolic','metabolism','respiration','energetic','macroscopic'], []),
 ('07-residuos-compostaje', ['compost','waste','residue','frass','manure','residuo'], []),
 ('04-gei-clima', ['greenhouse','emission','climate','ipcc','methane','carbon','inventario','atmospheric','nitrous','sostenible'], []),
]
def tema(txt):
    t = txt.lower()
    for carpeta, A, B in TEMAS:
        if any(k in t for k in A) and (not B or any(k in t for k in B)): return carpeta
    return '00-otros'

def yq(s): return '"' + str(s or '').replace('\\', '\\\\').replace('"', '\\"') + '"'
def anio(d):
    m = re.search(r'(19|20)\d{2}', d or '')
    return m.group(0) if m else 's.f.'

def nota(key, d, origen):
    donde = sorted(usadas.get(key, []))
    verificar = 'VERIFICAR' in (d.get('note') or '')
    fm = ['---', f'citekey: {key}', f'title: {yq(d.get("title"))}',
          'authors: [' + ', '.join(yq(a) for a in d.get('autores', [])) + ']',
          f'year: {anio(d.get("date") or d.get("year"))}', f'type: {d.get("type","?")}',
          f'doi: {yq(d.get("doi") or d.get("DOI") or "")}', f'url: {yq(d.get("url") or "")}',
          f'tema: {d["_tema"]}', 'tags: [' + ', '.join(yq(t) for t in d.get('tags', [])) + ']',
          f'pdf: {str(d["_pdf"]).lower()}', f'citado_tesis: {str(bool(donde)).lower()}',
          f'origen: {origen}' + ('\nverificar: true' if verificar else ''), '---']
    cuerpo = [f'# {d.get("title","(sin título)")}', '',
              f'- **Citekey:** `{key}`  - **Año:** {anio(d.get("date") or d.get("year"))}  - **Tipo:** {d.get("type","?")}',
              (f'- **DOI:** [{d.get("doi") or d.get("DOI")}](https://doi.org/{d.get("doi") or d.get("DOI")})' if (d.get("doi") or d.get("DOI")) else '- **DOI:** —'),
              ('> ⚠️ **VERIFICAR metadata contra fuente original**' if verificar else ''), '',
              '## Resumen', '', d.get('abstractNote') or d.get('abstract') or '_(sin resumen)_', '',
              '## Citado en la tesis', '']
    cuerpo += [f'- `{x}`' for x in donde] if donde else ['_(aún no citado)_']
    cuerpo += ['', '## Notas de lectura', '', '- [ ] Leído completo', '- [ ] Fichado', '']
    return '\n'.join(x for x in fm if x) + '\n\n' + '\n'.join(cuerpo)

if VAULT.exists(): shutil.rmtree(VAULT)
VAULT.mkdir(parents=True)
n_pdf = n_cit = n_dup = 0
usados_bib = set()
sin_key = []
por_tema, por_anio = {}, {}

for iid, d in items.items():
    key = {797: 'tiriaACTUALIZACIONCONTRIBUCIONDETERMINADA'}.get(iid) or bib_doi.get(norm_doi(d.get('DOI'))) or bib_tit.get(norm_tit(d.get('title')))
    if not key:
        key = f'zotero-sin-citekey-{iid}'; sin_key.append((iid, d.get('title', '')[:70]))
    if key in usados_bib:
        key = f'{key}-dup{iid}'; n_dup += 1
    usados_bib.add(key)
    d['_pdf'] = iid in pdfs
    d['_tema'] = tema(' '.join([d.get('title') or '', d.get('abstractNote') or '', ' '.join(d.get('tags', []))]))
    (VAULT/d['_tema']).mkdir(exist_ok=True)
    (VAULT/d['_tema']/f'{key}.md').write_text(nota(key, d, 'zotero'), encoding='utf-8')
    por_tema.setdefault(d['_tema'], []).append((key, d.get('title', ''), anio(d.get('date'))))
    por_anio.setdefault(anio(d.get('date')), []).append(key)
    n_pdf += d['_pdf']; n_cit += bool(usadas.get(key))

for key, f in bib_rec.items():
    if key in usados_bib: continue
    d = {'title': f.get('title',''), 'date': f.get('year',''), 'type': f.get('type',''),
         'doi': f.get('doi',''), 'url': f.get('url',''), 'note': f.get('note',''),
         'autores': [a.strip() for a in f.get('author','').split(' and ') if a.strip()], 'tags': [],
         'abstract': f.get('abstract',''), '_pdf': False}
    d['_tema'] = tema(d['title'])
    (VAULT/d['_tema']).mkdir(exist_ok=True)
    (VAULT/d['_tema']/f'{key}.md').write_text(nota(key, d, 'bib-manual'), encoding='utf-8')
    por_tema.setdefault(d['_tema'], []).append((key, d['title'], anio(d['date'])))
    por_anio.setdefault(anio(d['date']), []).append(key)
    n_cit += bool(usadas.get(key))

total = sum(len(v) for v in por_tema.values())
rd = ['# Vault bibliográfico — Tesis BSF-GEI', '',
      f'**{total} notas** | con PDF: {n_pdf} | citadas en la tesis: {n_cit}', '',
      '## Por tema', '']
for t in sorted(por_tema):
    rd.append(f'### {t} ({len(por_tema[t])})')
    rd += [f'- [[{t}/{k}]] — {ti[:80]} ({a})' for k, ti, a in sorted(por_tema[t], key=lambda x: x[2])] + ['']
rd += ['## Por año', ''] + [f'- **{a}**: {len(k)}' for a, k in sorted(por_anio.items())]
(VAULT/'README.md').write_text('\n'.join(rd), encoding='utf-8')
print(f'Listo: {total} notas | pdf {n_pdf} | citadas {n_cit} | sin citekey {len(sin_key)} | dups {n_dup}')
for t in sorted(por_tema): print(f'  {t}: {len(por_tema[t])}')
for iid, t in sin_key: print(f'  SIN KEY ({iid}): {t}')
