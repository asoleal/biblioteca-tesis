# buscar.py v2 — búsqueda transversal por grupos de sinónimos (ES/EN)
# uso:  python3 ~/buscar.py medicion co2 hermetia
#       python3 ~/buscar.py solucion numerica modelo --nota <citekey>
import re, shutil, sqlite3, subprocess, sys, tempfile
from pathlib import Path

HOME = Path.home()
BIB = HOME/'Zotero/Tesis_profesor_leal.bib'
CACHE = HOME/'.cache/tesis-textos'; CACHE.mkdir(parents=True, exist_ok=True)

args = []
_skip = False
for a in sys.argv[1:]:
    if a.startswith('--'): _skip = True; continue
    if _skip: _skip = False; continue
    args.append(a)
nota = sys.argv[sys.argv.index('--nota')+1] if '--nota' in sys.argv else None
N = int(sys.argv[sys.argv.index('--n')+1]) if '--n' in sys.argv else 8
if not args and not nota: sys.exit('Uso: buscar.py <términos> [--nota citekey] [--n N]')

EXP = {
 'co2': ['co2', 'carbon dioxide', 'dióxido de carbono'],
 'ch4': ['ch4', 'methane', 'metano'],
 'bsf': ['hermetia', 'black soldier', 'bsf', 'soldier fly', 'mosca soldado'],
 'n2o': ['n2o', 'nitrous', 'óxido nitroso'],
 'nh3': ['nh3', 'ammonia', 'amoníaco'],
 'gemelo': ['digital twin', 'gemelo'],
 'deb': ['dynamic energy budget', 'bioenergetic', 'energética'],
 'medicion': ['measurement', 'measuring', 'measure', 'monitoring', 'flux', 'medición', 'medicion'],
 'medición': ['measurement', 'measuring', 'measure', 'monitoring', 'flux', 'medición', 'medicion'],
 'emision': ['emission', 'emissions', 'emisión', 'emisiones'],
 'emisión': ['emission', 'emissions', 'emisión', 'emisiones'],
 'proceso': ['process', 'treatment', 'bioconversion', 'rearing', 'proceso'],
 'modelo': ['model', 'modeling', 'modelling', 'modelo'],
 'solucion': ['solution', 'solver', 'numerical', 'analytical', 'solución'],
 'sensor': ['sensor', 'ndir', 'sensing'],
 'iot': ['iot', 'internet of things'],
 'lote': ['batch', 'lote', 'fed-batch'],
 'batch': ['batch', 'lote', 'fed-batch'],
 'alimentacion': ['feeding', 'feed', 'diet', 'substrate'],
 'alimentación': ['feeding', 'feed', 'diet', 'substrate'],
 'sustrato': ['substrate', 'diet', 'feed'],
 'parametros': ['parameter', 'fitting', 'fitted', 'calibrat', 'estimat'],
 'parametro': ['parameter', 'fitting', 'fitted', 'calibrat', 'estimat'],
 'numerica': ['numerical', 'numeric', 'ode', 'integrat', 'solv'],
 'calibracion': ['calibrat', 'fitting', 'parameter'],
}
grupos = [EXP.get(a.lower(), [a.lower()]) for a in args]

def norm_doi(d): return re.sub(r'^https?://(dx\.)?doi\.org/', '', (d or '').lower().strip())
def norm_tit(t): return ' '.join(re.sub(r'[^a-z0-9 ]', ' ', (t or '').lower()).split())
bib = BIB.read_text(encoding='utf-8', errors='ignore')
CAMPO = r'(\w+)\s*=\s*\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}'
bdoi, btit = {}, {}
for typ, key, body in re.findall(r'@(\w+)\{([^,]+),(.*?)\n\}', bib, re.S):
    f = dict(re.findall(CAMPO, body))
    if f.get('doi'): bdoi[norm_doi(f['doi'])] = key
    if f.get('title'): btit.setdefault(norm_tit(f['title']), key)

tmp = Path(tempfile.mkdtemp())
for f in (HOME/'Zotero').glob('zotero.sqlite*'): shutil.copy(f, tmp/f.name)
db = sqlite3.connect(tmp/'zotero.sqlite'); db.row_factory = sqlite3.Row
items = {}
for r in db.execute("""SELECT i.itemID FROM items i JOIN itemTypes it ON i.itemTypeID=it.itemTypeID
  JOIN libraries l ON i.libraryID=l.libraryID AND l.type='group'
  WHERE it.typeName NOT IN ('attachment','note') AND i.itemID NOT IN (SELECT itemID FROM deletedItems)"""):
    items[r['itemID']] = {}
for r in db.execute("SELECT d.itemID, f.fieldName, v.value FROM itemData d JOIN fields f ON d.fieldID=f.fieldID JOIN itemDataValues v ON d.valueID=v.valueID"):
    if r['itemID'] in items: items[r['itemID']][r['fieldName']] = r['value']
ck = {i: (bdoi.get(norm_doi(d.get('DOI'))) or btit.get(norm_tit(d.get('title'))) or f'item-{i}') for i, d in items.items()}
tit = {ck[i]: d.get('title', '?') for i, d in items.items()}
absx = {ck[i]: d.get('abstractNote', '') for i, d in items.items()}

adj = {}
for r in db.execute("""SELECT ia.parentItemID p, ia.path, ai.key k FROM itemAttachments ia
  JOIN items ai ON ia.itemID=ai.itemID WHERE ia.contentType='application/pdf' AND ia.parentItemID IS NOT NULL"""):
    fn = (r['path'] or '').replace('storage:', '')
    if fn and ck.get(r['p']): adj.setdefault(ck.get(r['p']), HOME/'Zotero/storage'/r['k']/fn)

pdftotext = shutil.which('pdftotext')
if not pdftotext and not any(CACHE.glob('*.txt')):
    print('⚠️  falta pdftotext: sudo pacman -S poppler\n')

textos = {}
for key, pdf in adj.items():
    if not pdf or not pdf.exists(): continue
    out = CACHE/f'{key}.txt'
    if not out.exists() and pdftotext:
        subprocess.run([pdftotext, '-q', str(pdf), str(out)], check=False)
    if out.exists():
        t = out.read_text(encoding='utf-8', errors='ignore')
        corte = max(t.rfind('\nReferences'), t.rfind('\nReferencias'), t.rfind('\nREFERENCES'))
        textos[key] = t[:corte] if corte > len(t)*0.4 else t

if nota:
    cand = [k for k in set(list(textos) + list(tit)) if nota.lower() in k.lower()]
    if not cand: sys.exit(f'no encontré la nota {nota}')
    textos = {k: v for k, v in textos.items() if k in cand}
    tit = {k: v for k, v in tit.items() if k in cand}
    absx = {k: v for k, v in absx.items() if k in cand}
    print(f'>> dentro de: {cand}\n')

res = []
for key in set(list(textos) + list(tit)):
    cab = (tit.get(key, '') + ' ' + absx.get(key, '')).lower()
    chunks = [c.strip() for c in re.split(r'\n\s*\n', textos.get(key, '')) if len(c.strip()) > 80]
    ghit, score, tops = 0, 0, []
    for g in grupos:
        s_cab = sum(cab.count(t) for t in g)
        s_chunks = [(sum(c.lower().count(t) for t in g), c) for c in chunks]
        s_chunks = [x for x in s_chunks if x[0] > 0]
        s_txt = sum(s for s, _ in s_chunks)
        if s_cab + s_txt > 0:
            ghit += 1
            score += min(s_cab, 5)*3 + min(s_txt, 10)
            tops += s_chunks
    if ghit == 0: continue
    tops.sort(key=lambda x: -x[0])
    res.append((ghit, score, key, tops[:2]))

min_grupos = len(grupos) if len(grupos) <= 3 else len(grupos)-1
completos = [r for r in res if r[0] >= min_grupos]
parciales = [r for r in res if r[0] < min_grupos]
completos.sort(key=lambda x: -x[1]); parciales.sort(key=lambda x: (-x[0], -x[1]))

print(f'{len(completos)} documentos tocan TODOS los grupos | {len(parciales)} parciales')
print('grupos:', ['+'.join(g[:2]) for g in grupos], '\n')
for ghit, score, key, tops in (completos + parciales)[:N]:
    print(f'■ [{score:4d}|{ghit}/{len(grupos)}] {key} — {tit.get(key,"")[:85]}')
    for s, c in tops:
        low = c.lower()
        pos = min([low.find(t) for g in grupos for t in g if low.find(t) >= 0] or [0])
        frag = re.sub(r'\s+', ' ', c[max(0, pos-120):pos+280])
        print(f'    [{s:3d}] …{frag}…')
    print()
