#!/usr/bin/env python3
"""Pase 2: prueba TODAS las ubicaciones OA de Unpaywall por item."""
import logging, re, sqlite3, unicodedata, time
from pathlib import Path
import requests

EMAIL = "jlealgom@unal.edu.co"
GRUPO = "5844601"
API = f"http://localhost:23119/api/groups/{GRUPO}"
BASE = Path("/mnt/Compartida/Descargas_HDD/tesis-doctorado/biblioteca-local")
PDFS, DB, LOG = BASE/"pdfs", BASE/"pipeline.db", BASE/"logs"/"recuperar2.log"
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
           "Accept": "application/pdf,text/html;q=0.9,*/*;q=0.8"}

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG), logging.StreamHandler()])
log = logging.getLogger("recuperar2")

def slug(texto, n=40):
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", re.sub(r"<[^>]+>", "", t).lower()).strip("_")[:n]

def items(url):
    out, start = [], 0
    while True:
        r = requests.get(url, params={"limit": 100, "start": start}, timeout=30)
        r.raise_for_status(); lote = r.json()
        if not lote: break
        out.extend(lote); start += 100
    return out

def intentar_pdf(url, sesion):
    try:
        r = sesion.get(url, timeout=90, headers=HEADERS, allow_redirects=True)
        if r.status_code == 200 and r.content[:4] == b"%PDF":
            return r.content
    except Exception:
        pass
    return None

def main():
    conn = sqlite3.connect(DB)
    ya = {r[0] for r in conn.execute("SELECT key FROM zotero_map WHERE pdf IS NOT NULL")}
    arts = [i for i in items(f"{API}/items/top") if i["data"].get("itemType") == "journalArticle"]
    pendientes = [i for i in arts if i["data"]["key"] not in ya and i["data"].get("DOI")]
    log.info("Pendientes con DOI (pase 2): %d", len(pendientes))
    ok = 0
    sesion = requests.Session()
    for it in pendientes:
        d = it["data"]; key = d["key"]
        try:
            u = requests.get(f"https://api.unpaywall.org/v2/{d['DOI']}",
                             params={"email": EMAIL}, timeout=30).json()
            candidatas = [loc.get("url_for_pdf") for loc in u.get("oa_locations", [])]
            candidatas = [c for c in candidatas if c]
            contenido = None
            for url in candidatas:
                contenido = intentar_pdf(url, sesion)
                if contenido: break
                time.sleep(1)
            if not contenido:
                log.info("SIN ÉXITO: %s", d.get("title","")[:60]); continue
            m = re.search(r"(19|20)\d{2}", d.get("date") or "")
            año = m.group(0) if m else "sdfa"
            autor = (d.get("creators") or [{}])[0].get("lastName", "anon")
            nombre = f"{slug(autor)}_{año}_{slug(d.get('title',''), 35)}.pdf"
            (PDFS/nombre).write_bytes(contenido)
            conn.execute("INSERT OR REPLACE INTO zotero_map(key,pdf,titulo,doi,año) VALUES(?,?,?,?,?)",
                         (key, nombre, d.get("title",""), d["DOI"], año))
            conn.commit(); ok += 1
            log.info("RECUPERADO: %s", nombre)
        except Exception as e:
            log.warning("ERROR %s: %s", key, e)
    log.info("=== PASE 2: recuperados=%d de %d ===", ok, len(pendientes))
    conn.close()

if __name__ == "__main__":
    main()
