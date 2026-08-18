# export_biblio.py — exporta el catálogo del grupo Zotero a CSV (diagnósticos)
import csv, shutil, sqlite3, tempfile
from pathlib import Path
HOME = Path.home()
tmp = Path(tempfile.mkdtemp())
for f in (HOME/'Zotero').glob('zotero.sqlite*'): shutil.copy(f, tmp/f.name)
db = sqlite3.connect(tmp/'zotero.sqlite'); db.row_factory = sqlite3.Row
items = {}
for r in db.execute("""SELECT i.itemID, i.key, it.typeName FROM items i
  JOIN itemTypes it ON i.itemTypeID=it.itemTypeID
  JOIN libraries l ON i.libraryID=l.libraryID AND l.type='group'
  WHERE it.typeName NOT IN ('attachment','note')
  AND i.itemID NOT IN (SELECT itemID FROM deletedItems)"""):
    items[r['itemID']] = {'key': r['key'], 'itemType': r['typeName']}
for r in db.execute("SELECT d.itemID, f.fieldName, v.value FROM itemData d JOIN fields f ON d.fieldID=f.fieldID JOIN itemDataValues v ON d.valueID=v.valueID"):
    if r['itemID'] in items: items[r['itemID']][r['fieldName']] = r['value']
nuevo = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='creatorData'").fetchone() is None
qc = ("SELECT ic.itemID, c.lastName, c.firstName FROM itemCreators ic JOIN creators c ON ic.creatorID=c.creatorID ORDER BY ic.itemID, ic.orderIndex" if nuevo else
      "SELECT ic.itemID, cd.lastName, cd.firstName FROM itemCreators ic JOIN creators c ON ic.creatorID=c.creatorID JOIN creatorData cd ON c.creatorDataID=cd.creatorDataID ORDER BY ic.itemID, ic.orderIndex")
for r in db.execute(qc):
    if r['itemID'] in items:
        nom = (r['lastName'] or '') + (', ' + r['firstName'] if r['firstName'] else '')
        if nom.strip(): items[r['itemID']].setdefault('autores', []).append(nom.strip(', '))
for r in db.execute("SELECT it.itemID, t.name FROM itemTags it JOIN tags t ON it.tagID=t.tagID"):
    if r['itemID'] in items: items[r['itemID']].setdefault('tags', []).append(r['name'])
for r in db.execute("SELECT ci.itemID, c.collectionName FROM collectionItems ci JOIN collections c ON ci.collectionID=c.collectionID"):
    if r['itemID'] in items: items[r['itemID']].setdefault('collections', []).append(r['collectionName'])
pdfs = {}
for r in db.execute("""SELECT ia.parentItemID p, ai.key||'/'||REPLACE(ia.path,'storage:','') fp
  FROM itemAttachments ia JOIN items ai ON ia.itemID=ai.itemID
  WHERE ia.contentType='application/pdf' AND ia.parentItemID IS NOT NULL"""):
    pdfs.setdefault(r['p'], r['fp'])
out = HOME/'biblioteca.csv'
with open(out, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['itemID','key','itemType','title','abstractNote','date','DOI','url','authors','tags','collections','pdf_path'])
    for iid, d in items.items():
        w.writerow([iid, d.get('key',''), d.get('itemType',''), d.get('title',''), d.get('abstractNote',''),
                    d.get('date',''), d.get('DOI',''), d.get('url',''), '; '.join(d.get('autores',[])),
                    '; '.join(d.get('tags',[])), '; '.join(d.get('collections',[])), pdfs.get(iid,'')])
print(f'{len(items)} ítems → {out}')
