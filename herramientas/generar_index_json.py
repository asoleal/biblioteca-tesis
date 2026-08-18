# generar_index_json.py — convierte vault .md → vault_index.json (para la webapp)
import json, re, sys
from pathlib import Path
VAULT = Path(sys.argv[1]) / 'vault'

def val(s):
    s = s.strip()
    if s.startswith('[') or s.startswith('"'):
        try: return json.loads(s)
        except Exception: pass
    if s in ('true', 'false'): return s == 'true'
    return s

notas = []
for md in sorted(VAULT.rglob('*.md')):
    if md.name == 'README.md': continue
    txt = md.read_text(encoding='utf-8')
    m = re.match(r'---\n(.*?)\n---\n', txt, re.S)
    if not m: continue
    fm = {}
    for line in m.group(1).split('\n'):
        mm = re.match(r'(\w+):\s*(.*)', line)
        if mm: fm[mm.group(1)] = val(mm.group(2))
    ab = re.search(r'## Resumen\n\n(.*?)\n\n## Citado', txt, re.S)
    notas.append({
        'citekey': fm.get('citekey',''), 'title': fm.get('title',''),
        'authors': fm.get('authors',[]), 'year': str(fm.get('year','')),
        'type': fm.get('type',''), 'doi': fm.get('doi',''), 'url': fm.get('url',''),
        'tema': fm.get('tema',''), 'tags': fm.get('tags',[]),
        'pdf': bool(fm.get('pdf')), 'citado': bool(fm.get('citado_tesis')),
        'verificar': bool(fm.get('verificar')),
        'abstract': (ab.group(1) if ab and 'sin resumen' not in ab.group(1) else ''),
        'citado_en': re.findall(r'^- `(.+?)`', txt, re.M),
        'path': str(md.relative_to(VAULT)),
    })
(VAULT/'vault_index.json').write_text(json.dumps(notas, ensure_ascii=False, indent=1), encoding='utf-8')
print(f'Listo: {len(notas)} notas → {VAULT}/vault_index.json')
