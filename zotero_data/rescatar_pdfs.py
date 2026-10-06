#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rescatar_pdfs.py — TERCERA PASADA sobre los no_conseguido de reporte_pdfs.csv.

Estrategias (todas legales, OA):
  A. DOI reconstruido/verificado (mapa curado) -> Unpaywall/OpenAlex.
  B. DOI extraído de la columna `url` (PLOS, SAGE, OECD) -> Unpaywall/OpenAlex.
  C. URL MDPI -> variante /pdf directa.
  D. Descarga directa de URLs .pdf de la columna `url` (UNFCCC, WMO, Verra,
     FAO, IDEAM/Minambiente, Minciencias, repositorios, ScienceDirect CDN).
  E. URLs curadas (IPCC AR5/AR6, Banco Mundial) verificadas manualmente.
  F. Crossref (metadatos) por título -> DOI -> Unpaywall, para el resto.

Actualiza los checkpoints y REGENERA reporte_pdfs.csv / reporte_pdfs.md
fusionando con lo ya conseguido. Reutiliza la lógica de recuperar_pdfs_zotero.py
(debe estar en la misma carpeta).

Desviación documentada: se añaden las fuentes `url_directa`, `crossref` y
`curado` (además de unpaywall/openalex del procedimiento original) y la API de
metadatos de Crossref (legal, solo metadatos; el PDF siempre sale de una
ubicación OA reportada por Unpaywall/OpenAlex o del sitio oficial).
"""

import csv
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import recuperar_pdfs_zotero as R  # noqa: E402

import requests  # noqa: E402

# ---------------------------------------------------------------------------
# A. DOIs reconstruidos y VERIFICADOS como OA (Unpaywall, 2026-07-19)
# ---------------------------------------------------------------------------
MAPA_DOIS = {
    "567": "10.1371/journal.pone.0276605",      # PLOS ONE (OA)
    "612": "10.1038/s41598-024-77430-6",        # Scientific Reports (OA)
    "319": "10.1186/s12302-024-00861-5",        # Environ. Sciences Europe (OA)
    "264": "10.3390/su152215889",               # Kabange et al. 2023, Sustainability (OA)
    "333": "10.3389/fsufs.2021.709993",         # Frontiers in Sustainable Food Systems (OA)
    "340": "10.3389/fphy.2021.734447",          # Frontiers in Physiology (OA)
    "110": "10.1787/59cf6c95-en",               # OECD Beyond food loss... (OA)
}

# ---------------------------------------------------------------------------
# E. URLs curadas (verificadas 2026-07-19; sitios oficiales, acceso abierto)
# ---------------------------------------------------------------------------
CURADAS = {
    "174": "https://www.ipcc.ch/site/assets/uploads/2018/02/ipcc_wg3_ar5_full.pdf",
    "198": "https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_Chapter07.pdf",
    "120": "https://openknowledge.worldbank.org/server/api/core/bitstreams/bdd449bb-c298-4eb7-a794-c80bfe209f4a/content",
    "350": "https://openknowledge.worldbank.org/server/api/core/bitstreams/bdd449bb-c298-4eb7-a794-c80bfe209f4a/content",
    "126": "https://wmo.int/sites/default/files/2025-10/GHG-21_en.pdf",
}

PATRON_DOI_URL = re.compile(r"(10\.\d{4,5}/[^\s?&#]+)")
OECD_ID = re.compile(r"_([a-z0-9]{8})-en")

# ISSN MDPI -> slug usado por su CDN mdpi-res.com (sirve el PDF sin bloqueo anti-bot)
MDPI_SLUG = {"2071-1050": "sustainability", "2218-1989": "metabolites"}
MDPI_PAT = re.compile(r"mdpi\.com/(\d{4}-\d{3}[\dX])/(\d+)/(\d+)/(\d+)")


def alternativas_descarga(url: str):
    """Genera URLs alternativas anti-bloqueo para un candidato."""
    alt = []
    m = MDPI_PAT.search(url)
    if m and m.group(1) in MDPI_SLUG:
        s = MDPI_SLUG[m.group(1)]
        for art in (m.group(4).zfill(5), m.group(4)):  # MDPI rellena a 5 dígitos
            alt.append(f"https://mdpi-res.com/d_attachment/{s}/{s}-{m.group(2)}-{art}"
                       f"/article_deploy/{s}-{m.group(2)}-{art}.pdf")
    m3 = re.search(r"(10\.3389/[^\s?&#]+)", url)  # Frontiers: patrón directo /pdf
    if m3:
        alt.append(f"https://www.frontiersin.org/articles/{m3.group(1)}/pdf")
    m4 = re.search(r"(10\.1371/journal\.[a-z]+\.\d+)", url)  # PLOS: printable directo
    if m4:
        alt.append(f"https://journals.plos.org/plosone/article/file?id={m4.group(1)}&type=printable")
    m2 = re.search(r"pmc\.ncbi\.nlm\.nih\.gov/articles/(PMC\d+)", url)
    if m2:
        alt.append(f"https://europepmc.org/backend/ptpmcrender.fcgi?accid={m2.group(1)}&blobtype=pdf")
    return alt


def candidatos_fila(row):
    """Genera [(fuente, url)] para una fila no_conseguido."""
    iid = str(row["itemID"]).strip()
    titulo = row.get("title", "")
    url_col = (row.get("url") or "").strip()
    cand = []

    # A. DOI curado
    if iid in MAPA_DOIS:
        cand += [("unpaywall", u) for u in R.fuente_unpaywall(MAPA_DOIS[iid])[0]]
        cand += [("openalex", u) for u in R.fuente_openalex_doi(MAPA_DOIS[iid])]

    # B. DOI embebido en la columna url (PLOS, SAGE, MDPI, etc.)
    if not cand and url_col:
        m = PATRON_DOI_URL.search(url_col)
        if m:
            doi = m.group(1).rstrip(".")
            cand += [("unpaywall", u) for u in R.fuente_unpaywall(doi)[0]]
            cand += [("openalex", u) for u in R.fuente_openalex_doi(doi)]
        elif OECD_ID.search(url_col):  # OECD sin DOI explícito en la URL
            cand += [("unpaywall", u)
                     for u in R.fuente_unpaywall(f"10.1787/{OECD_ID.search(url_col).group(1)}-en")[0]]

    # C. MDPI página -> PDF directo
    if not cand and "mdpi.com/" in url_col and not url_col.rstrip("/").endswith("/pdf"):
        cand.append(("url_directa", url_col.rstrip("/") + "/pdf"))

    # D. Descarga directa de URLs .pdf / sitios oficiales
    if not cand and url_col:
        es_pdf = url_col.lower().split("?")[0].endswith(".pdf")
        dominios_ok = ("unfccc.int", "wmo.int", "verra.org", "fao.org", "minambiente.gov.co",
                       "minciencias.gov.co", "ideam.gov.co", "ipcc.ch", "eprints.",
                       "sciencedirectassets.com", "scholarcommons.", "constantvzw.org",
                       "yellowdragonblog.com", "openknowledge.")
        if es_pdf or any(d in url_col for d in dominios_ok):
            cand.append(("url_directa", url_col))

    # E. Curadas
    if not cand and iid in CURADAS:
        cand.append(("curado", CURADAS[iid]))

    # F. Crossref por título -> DOI -> Unpaywall/OpenAlex
    if not cand and R.norm_title(titulo) and " " in titulo.strip():
        doi = crossref_buscar(titulo)
        if doi:
            cand += [("crossref", u) for u in R.fuente_unpaywall(doi)[0]]
            cand += [("openalex", u) for u in R.fuente_openalex_doi(doi)]
    return cand


def crossref_buscar(titulo):
    """Crossref (metadatos): devuelve DOI solo si el título normalizado coincide."""
    objetivo = R.norm_title(titulo)
    try:
        R.RATE.wait("crossref")
        r = requests.get(
            "https://api.crossref.org/works?query.bibliographic="
            + requests.utils.quote(titulo) + "&rows=3&mailto=" + R.EMAIL,
            headers=R.UA, timeout=R.TIMEOUT)
        if r.status_code != 200:
            return None
        for item in r.json()["message"]["items"]:
            t = R.norm_title((item.get("title") or [""])[0])
            if t and (objetivo in t or t in objetivo):
                return item.get("DOI")
    except requests.RequestException:
        pass
    return None


def main():
    R.DIR_PDF.mkdir(parents=True, exist_ok=True)
    R.DIR_CKPT.mkdir(parents=True, exist_ok=True)
    # Filas objetivo: las que siguen no_conseguido tras la 2ª pasada
    estado = {}
    if R.REPORTE_CSV.exists():
        with open(R.REPORTE_CSV, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                estado[r["itemID"]] = r["estado"]

    with open(R.CSV_IN, newline="", encoding="utf-8-sig") as f:
        filas = [r for r in csv.DictReader(f)
                 if estado.get(str(r["itemID"]).strip(), "no_conseguido") != "conseguido"]
    print(f"Objetivo de rescate: {len(filas)} filas no_conseguido")

    nuevos = 0
    for i, row in enumerate(filas, 1):
        iid = str(row["itemID"]).strip()
        cand = candidatos_fila(row)
        ok = None
        archivo = R.DIR_PDF / R.nombre_archivo(row)
        for fuente, url in cand:
            for u in [url] + alternativas_descarga(url):
                if R.descargar_pdf(u, archivo):
                    ok = (fuente, u)
                    break
            if ok:
                break
        if ok:
            cp = {
                "itemID": iid, "primer_autor": R.primer_autor(row.get("author", "")),
                "año": R.anio(row.get("date", "")), "titulo": row.get("title", ""),
                "DOI": (row.get("DOI") or MAPA_DOIS.get(iid, "")).strip(),
                "estado": "conseguido", "fuente": ok[0], "url_pdf": ok[1],
                "archivo_local": str(archivo), "motivo_fallo": "",
            }
            R.ckpt_path(iid).write_text(json.dumps(cp, ensure_ascii=False, indent=1),
                                        encoding="utf-8")
            nuevos += 1
            print(f"[{i:3d}/{len(filas)}] RESCATADO ({ok[0]:12s}) {row['title'][:60]}")
        else:
            print(f"[{i:3d}/{len(filas)}] sigue sin PDF        {row['title'][:60]}")

    # Regenerar reportes fusionados desde TODOS los checkpoints
    registros = []
    for cp in sorted(R.DIR_CKPT.glob("*.json"), key=lambda p: int(p.stem)):
        try:
            registros.append(json.loads(cp.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            pass
    conseg = [r for r in registros if r["estado"] == "conseguido"]
    verif = R.verificar(conseg) if conseg else []
    n_ok, total, por_fuente, por_motivo = R.escribir_reportes(registros, verif)

    print("\n================ RESCATE ================")
    print(f"Nuevos rescatados: {nuevos}")
    print(f"TOTAL ahora: {n_ok}/{total}")
    print("Por fuente:", json.dumps(por_fuente, ensure_ascii=False))
    print("Por motivo de fallo:", json.dumps(por_motivo, ensure_ascii=False))


if __name__ == "__main__":
    main()
