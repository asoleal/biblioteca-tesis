#!/usr/bin/env python3
"""Inventario del grupo Zotero + cruce con pipeline.db (solo lectura)."""
import sqlite3, requests
from pathlib import Path

GRUPO = "5844601"
API = f"http://localhost:23119/api/groups/{GRUPO}"
DB = Path("/mnt/Compartida/Descargas_HDD/tesis-doctorado/biblioteca-local/pipeline.db")

def todos_los_items():
    items, start = [], 0
    while True:
        r = requests.get(f"{API}/items/top", params={"limit": 100, "start": start}, timeout=30)
        r.raise_for_status()
        lote = r.json()
        if not lote: break
        items.extend(lote); start += 100
    return items

def main():
    items = todos_los_items()
    conn = sqlite3.connect(DB)
    indexados = {r[0] for r in conn.execute("SELECT source FROM indexed")}

    articulos = [i for i in items if i["data"].get("itemType") == "journalArticle"]
    print(f"Total items top-level: {len(items)} | journalArticle: {len(articulos)}\n")
    print(f"{'KEY':10} {'AÑO':6} {'DOI':12} TÍTULO")
    print("-" * 90)
    sin_doi = 0
    for it in sorted(articulos, key=lambda x: x["data"].get("date", "")):
        d = it["data"]
        doi = d.get("DOI", "")
        if not doi: sin_doi += 1
        año = (d.get("date") or "")[:4]
        titulo = (d.get("title") or "")[:60]
        print(f"{d['key']:10} {año:6} {'SÍ' if doi else 'NO':12} {titulo}")
    print("-" * 90)
    print(f"Artículos SIN DOI: {sin_doi}")
    print(f"\nDocumentos ya indexados en Qdrant: {len(indexados)}")
    for s in sorted(indexados): print(f"  - {s}")
    conn.close()

if __name__ == "__main__":
    main()
