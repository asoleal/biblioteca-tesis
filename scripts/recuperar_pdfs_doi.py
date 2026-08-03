#!/usr/bin/env python3
"""Recupera PDFs faltantes vía DOI -> Unpaywall (acceso abierto). Idempotente."""
import logging, re, sqlite3, unicodedata
from pathlib import Path
import requests

EMAIL = "jlealgom@unal.edu.co"  # requerido por la API de Unpaywall
GRUPO = "5844601"
API = f"http://localhost:23119/api/groups/{GRUPO}"
BASE = Path("/mnt/Compartida/Descargas_HDD/tesis-doctorado/biblioteca-local")
PDFS, DB, LOG = BASE/"pdfs", BASE/"pipeline.db", BASE/"logs"/"recuperar.log"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG), logging.StreamHandler()])
log = logging.getLogger("recuperar")

def slug(texto, n=40):
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = re.sub(r"<[^>]+>", "", t)
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
    ya = {r[0] for r in conn.execute("SELECT key FROM zotero_map WHERE pdf IS NOT NULL")}
    arts = [i for i in items(f"{API}/items/top") if i["data"].get("itemType") == "journalArticle"]
    pendientes = [i for i in arts if i["data"]["key"] not in ya]
    log.info("Pendientes de recuperar: %d", len(pendientes))
    ok, sin_doi, sin_oa = 0, 0, 0
    for it in pendientes:
        d = it["data"]; key = d["key"]; doi = d.get("DOI", "")
        if not doi:
            sin_doi += 1
            log.info("SIN DOI: %s", d.get("title","")[:60]); continue
        try:
            u = requests.get(f"https://api.unpaywall.org/v2/{doi}",
                             params={"email": EMAIL}, timeout=30).json()
            url_pdf = (u.get("best_oa_location") or {}).get("url_for_pdf")
            if not url_pdf:
                sin_oa += 1
                log.info("SIN OA: %s | %s", doi, d.get("title","")[:50]); continue
            año = (re.search(r"(19|20)\d{2}", d.get("date") or "") or [None])
            año = año.group(0) if hasattr(año, "group") else "sdfa"
            autor = (d.get("creators") or [{}])[0].get("lastName", "anon")
            nombre = f"{slug(autor)}_{año}_{slug(d.get('title',''), 35)}.pdf"
            r = requests.get(url_pdf, timeout=120,
                             headers={"User-Agent": "Mozilla/5.0"})
            if r.status_code == 200 and r.content[:4] == b"%PDF":
                (PDFS/nombre).write_bytes(r.content)
                conn.execute("INSERT OR REPLACE INTO zotero_map(key,pdf,titulo,doi,año) VALUES(?,?,?,?,?)",
                             (key, nombre, d.get("title",""), doi, año))
                conn.commit(); ok += 1
                log.info("RECUPERADO: %s", nombre)
            else:
                log.info("DESCARGA FALLÓ (%s): %s", r.status_code, nombre)
        except Exception as e:
            log.warning("ERROR %s: %s", doi, e)
    log.info("=== RESUMEN: recuperados=%d | sin DOI=%d | sin OA=%d ===", ok, sin_doi, sin_oa)
    conn.close()

if __name__ == "__main__":
    main()
