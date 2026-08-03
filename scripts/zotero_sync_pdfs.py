#!/usr/bin/env python3
"""Descarga adjuntos PDF del grupo Zotero -> pdfs/. Idempotente."""
import logging, re, sqlite3, unicodedata
from pathlib import Path
import requests

GRUPO = "5844601"
API = f"http://localhost:23119/api/groups/{GRUPO}"
BASE = Path("/mnt/Compartida/Descargas_HDD/tesis-doctorado/biblioteca-local")
PDFS, DB, LOG = BASE/"pdfs", BASE/"pipeline.db", BASE/"logs"/"zotero_sync.log"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG), logging.StreamHandler()])
log = logging.getLogger("zsync")

def slug(texto, n=40):
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = re.sub(r"<[^>]+>", "", t)  # quita tags html como <i>
    return re.sub(r"[^a-z0-9]+", "_", t.lower()).strip("_")[:n]

def items(url):
    out, start = [], 0
    while True:
        r = requests.get(url, params={"limit": 100, "start": start}, timeout=30)
        r.raise_for_status(); lote = r.json()
        if not lote: break
        out.extend(lote); start += 100
    return out

def main():
    conn = sqlite3.connect(DB)
    conn.execute("""CREATE TABLE IF NOT EXISTS zotero_map(
        key TEXT PRIMARY KEY, pdf TEXT, titulo TEXT, doi TEXT, año TEXT)""")
    arts = [i for i in items(f"{API}/items/top") if i["data"].get("itemType") == "journalArticle"]
    log.info("Artículos en el grupo: %d", len(arts))
    descargados = 0
    for it in arts:
        d = it["data"]; key = d["key"]
        if conn.execute("SELECT 1 FROM zotero_map WHERE key=? AND pdf IS NOT NULL", (key,)).fetchone():
            continue  # ya sincronizado
        # buscar adjunto PDF hijo
        hijos = requests.get(f"{API}/items/{key}/children", timeout=30).json()
        adj = [h for h in hijos if h["data"].get("contentType") == "application/pdf"]
        if not adj:
            log.info("SIN PDF: %s", d.get("title", "")[:60]); continue
        m = re.search(r"(19|20)\d{2}", d.get("date") or "")
        año = m.group(0) if m else "sdfa"
        autor = (d.get("creators") or [{}])[0].get("lastName", "anon")
        nombre = f"{slug(autor)}_{año}_{slug(d.get('title',''), 35)}.pdf"
        destino = PDFS / nombre
        if not destino.exists():
            try:
                r = requests.get(f"{API}/items/{adj[0]['key']}/file",
                                 timeout=120, allow_redirects=False)
                loc = r.headers.get("Location", "")
                if loc.startswith("file://"):
                    from urllib.parse import unquote, urlparse
                    import shutil
                    shutil.copy(unquote(urlparse(loc).path), destino)
                else:
                    destino.write_bytes(r.content)
                descargados += 1
                log.info("DESCARGADO: %s", nombre)
            except Exception as e:
                log.warning("ADJUNTO ROTO %s (%s): %s", key, nombre, e)
                continue  # no se registra en zotero_map: se reintentará la próxima vez
        conn.execute("INSERT OR REPLACE INTO zotero_map(key,pdf,titulo,doi,año) VALUES(?,?,?,?,?)",
                     (key, nombre, d.get("title",""), d.get("DOI",""), año))
        conn.commit()
    log.info("Descargas nuevas: %d. Total en pdfs/: %d", descargados, len(list(PDFS.glob('*.pdf'))))
    conn.close()

if __name__ == "__main__":
    main()
