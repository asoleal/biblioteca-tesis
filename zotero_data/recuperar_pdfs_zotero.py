#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
recuperar_pdfs_zotero.py
========================
Recupera PDFs de acceso abierto (legal) para los articulos listados en
/home/jjlealg/Zotero/faltantes.csv y genera los reportes requeridos.

Pipeline por registro:
  1. DOI -> Unpaywall (best_oa_location.url_for_pdf/.url si is_oa)
  2. DOI -> OpenAlex works/doi:{doi}
  3. Título exacto -> arXiv API
  4. Sin DOI -> OpenAlex search (validación título/año/autor)

Reglas implementadas:
  - Solo fuentes OA legales (Unpaywall, OpenAlex, arXiv).
  - Rate limit GLOBAL por API: 1 req/s (thread-safe).
  - Timeout 30 s, reintentos backoff 2/4/8 s (máx 3).
  - Validación de descarga: cabecera %PDF y tamaño > 20 KB.
  - Checkpoint JSON por itemID (reanudable).
  - No modifica nada fuera de las carpetas de salida.

Uso:
  python3 recuperar_pdfs_zotero.py            # procesa los pendientes
  python3 recuperar_pdfs_zotero.py --workers 4
"""

import csv
import html
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
import unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests

# ----------------------------------------------------------------------------
# Configuración
# ----------------------------------------------------------------------------
BASE = Path("/home/jjlealg/Zotero")
CSV_IN = BASE / "faltantes.csv"
DIR_PDF = BASE / "pdfs_descargados"
DIR_CKPT = BASE / ".checkpoint_pdfs"
REPORTE_CSV = BASE / "reporte_pdfs.csv"
REPORTE_MD = BASE / "reporte_pdfs.md"

EMAIL = "johnjairoleal@gmail.com"
UA = {"User-Agent": f"ZoteroRebuild/1.0 (mailto:{EMAIL})"}
TIMEOUT = 30
MIN_PDF_BYTES = 20 * 1024
MAX_WORKERS_DEFAULT = 4  # la concurrencia NO rompe el rate limit (es global por API)

UNPAYWALL = "https://api.unpaywall.org/v2/{doi}?email=" + EMAIL
OPENALEX_DOI = "https://api.openalex.org/works/doi:{doi}?mailto=" + EMAIL
OPENALEX_SEARCH = ("https://api.openalex.org/works?search={q}&per-page=5&mailto=" + EMAIL)
ARXIV_QUERY = 'https://export.arxiv.org/api/query?search_query=ti:"{t}"&max_results=3'
ARXIV_PDF = "https://arxiv.org/pdf/{aid}"

# ----------------------------------------------------------------------------
# Rate limiter global por API (1 petición/segundo por host lógico)
# ----------------------------------------------------------------------------
class RateLimiter:
    def __init__(self):
        self._lock = threading.Lock()
        self._last = {}

    def wait(self, api: str):
        with self._lock:
            now = time.monotonic()
            prev = self._last.get(api, 0.0)
            delta = now - prev
            if delta < 1.0:
                time.sleep(1.0 - delta)
            self._last[api] = time.monotonic()

RATE = RateLimiter()

# ----------------------------------------------------------------------------
# Utilidades
# ----------------------------------------------------------------------------
def norm_title(t: str) -> str:
    """Quita tags HTML, minúsculas, sin acentos, solo [a-z0-9 ], espacios colapsados."""
    t = html.unescape(t or "")
    t = re.sub(r"<[^>]+>", " ", t)
    t = t.lower()
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def primer_autor(author_field: str) -> str:
    a = (author_field or "").split(";")[0].strip()
    if "," in a:
        a = a.split(",")[0].strip()
    return a or "anon"


def anio(date_field: str) -> str:
    m = re.search(r"(19|20)\d{2}", date_field or "")
    return m.group(0) if m else "sf"


def doi_corto(doi: str, item_id: str) -> str:
    if doi:
        alnum = re.sub(r"[^A-Za-z0-9]", "", doi)
        if alnum:
            return alnum[-8:]
    return f"id{item_id}"


def nombre_archivo(row) -> str:
    pa = re.sub(r"[^A-Za-z0-9]", "", primer_autor(row.get("author", ""))) or "anon"
    return f"{pa}_{anio(row.get('date',''))}_{doi_corto(row.get('DOI','').strip(), row.get('itemID',''))}.pdf"


def get_json(url: str, api: str):
    """GET con rate limit, timeout 30 s y backoff 2/4/8 (máx 3 intentos)."""
    for intento, espera in enumerate((2, 4, 8), start=1):
        try:
            RATE.wait(api)
            r = requests.get(url, headers=UA, timeout=TIMEOUT)
            if r.status_code == 404:
                return None
            if r.status_code in (429, 500, 502, 503):
                if intento < 3:
                    time.sleep(espera)
                    continue
                return None
            r.raise_for_status()
            return r.json()
        except requests.RequestException:
            if intento < 3:
                time.sleep(espera)
    return None


def get_text(url: str, api: str):
    for intento, espera in enumerate((2, 4, 8), start=1):
        try:
            RATE.wait(api)
            r = requests.get(url, headers=UA, timeout=TIMEOUT)
            if r.status_code == 404:
                return None
            r.raise_for_status()
            return r.text
        except requests.RequestException:
            if intento < 3:
                time.sleep(espera)
    return None


UA_BROWSER = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "application/pdf,text/html;q=0.9,*/*;q=0.8",
}


def descargar_pdf(url: str, destino: Path) -> bool:
    """Descarga y valida (%PDF y > 20 KB). Devuelve True si es válido.
    Si el UA propio es bloqueado (anti-bot del editorial), reintenta con UA navegador."""
    tmp = destino.with_suffix(".part")
    for headers in (UA, UA_BROWSER):
        for intento, espera in enumerate((2, 4, 8), start=1):
            try:
                RATE.wait("descarga")
                with requests.get(url, headers=headers, timeout=TIMEOUT, stream=True) as r:
                    r.raise_for_status()
                    with open(tmp, "wb") as f:
                        for chunk in r.iter_content(65536):
                            f.write(chunk)
                ok = (tmp.stat().st_size > MIN_PDF_BYTES
                      and open(tmp, "rb").read(4) == b"%PDF")
                if ok:
                    tmp.replace(destino)
                    return True
                tmp.unlink(missing_ok=True)
                break  # contenido inválido: probar con el otro UA
            except requests.RequestException:
                if intento < 3:
                    time.sleep(espera)
    tmp.unlink(missing_ok=True)
    return False

# ----------------------------------------------------------------------------
# Fuentes OA
# ----------------------------------------------------------------------------
IMG_EXT = (".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff")


def _es_imagen(url: str) -> bool:
    return (url or "").split("?")[0].lower().endswith(IMG_EXT)


def fuente_unpaywall(doi: str):
    """Devuelve (lista_urls, is_oa | None). Recorre TODAS las oa_locations:
    best_oa_location a veces apunta a imágenes (p. ej. els-cdn .jpg)."""
    data = get_json(UNPAYWALL.format(doi=doi), "unpaywall")
    if data is None:
        return [], None
    if not data.get("is_oa"):
        return [], False
    urls, vistas = [], set()
    locs = ([data["best_oa_location"]] if data.get("best_oa_location") else []) \
        + (data.get("oa_locations") or [])
    for loc in locs:
        for u in (loc.get("url_for_pdf"), loc.get("url")):
            if u and u not in vistas:
                vistas.add(u)
                urls.append(u)
    urls.sort(key=_es_imagen)  # primero las que no parecen imagen
    return urls, True


def fuente_openalex_doi(doi: str):
    data = get_json(OPENALEX_DOI.format(doi=doi), "openalex")
    if not data:
        return []
    loc = data.get("best_oa_location") or {}
    urls = [loc.get("pdf_url"), (data.get("open_access") or {}).get("oa_url")]
    return [u for u in urls if u]


def fuente_arxiv(titulo: str):
    txt = get_text(ARXIV_QUERY.format(t=requests.utils.quote(titulo)), "arxiv")
    if not txt:
        return []
    objetivo = norm_title(titulo)
    entries = re.findall(r"<entry>(.*?)</entry>", txt, re.S)
    for e in entries:
        m_t = re.search(r"<title>(.*?)</title>", e, re.S)
        m_i = re.search(r"<id>https?://arxiv\.org/abs/([^<]+)</id>", e)
        if m_t and m_i and norm_title(m_t.group(1)) == objetivo:
            return [ARXIV_PDF.format(aid=m_i.group(1).strip())]
    return []


def fuente_openalex_search(row):
    """Solo para registros sin DOI. Valida título, año ±1 y apellido 1er autor."""
    data = get_json(OPENALEX_SEARCH.format(q=requests.utils.quote(row.get("title", ""))),
                    "openalex")
    if not data:
        return []
    objetivo = norm_title(row.get("title", ""))
    if not objetivo:
        return []
    apellido = norm_title(primer_autor(row.get("author", "")))
    try:
        anio_ref = int(anio(row.get("date", "")))
    except ValueError:
        anio_ref = None
    urls = []
    for w in data.get("results", []):
        t = norm_title(w.get("title") or "")
        if objetivo not in t and t not in objetivo:
            continue
        if anio_ref and w.get("publication_year"):
            if abs(w["publication_year"] - anio_ref) > 1:
                continue
        if apellido:
            auths = w.get("authorships") or []
            nom0 = norm_title((auths[0].get("author") or {}).get("display_name", "")) if auths else ""
            if apellido not in nom0:
                continue
        loc = w.get("best_oa_location") or {}
        for u in (loc.get("pdf_url"), (w.get("open_access") or {}).get("oa_url")):
            if u and u not in urls:
                urls.append(u)
    return urls

# ----------------------------------------------------------------------------
# Procesamiento por artículo (con checkpoint)
# ----------------------------------------------------------------------------
def ckpt_path(item_id: str) -> Path:
    return DIR_CKPT / f"{item_id}.json"


def procesar(row):
    item_id = str(row.get("itemID", "")).strip()
    titulo = row.get("title", "")
    doi = (row.get("DOI") or "").strip()
    base = {
        "itemID": item_id,
        "primer_autor": primer_autor(row.get("author", "")),
        "año": anio(row.get("date", "")),
        "titulo": titulo,
        "DOI": doi,
        "estado": "no_conseguido",
        "fuente": "",
        "url_pdf": "",
        "archivo_local": "",
        "motivo_fallo": "",
    }
    cp = ckpt_path(item_id)
    if cp.exists():  # reanudar sin repetir
        try:
            return json.loads(cp.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass

    archivo = DIR_PDF / nombre_archivo(row)
    is_oa_unpaywall = None
    hubo_candidatos = False
    ultimo_lote = []
    ok = None  # (fuente, url) de la descarga validada

    def intentar(lote):
        """Intenta descargar cada candidato del lote hasta validar uno."""
        nonlocal hubo_candidatos, ultimo_lote
        if lote:
            hubo_candidatos = True
            ultimo_lote = lote
        for fuente, url in lote:
            if descargar_pdf(url, archivo):
                return (fuente, url)
        return None

    # 1) Unpaywall -> 2) OpenAlex DOI -> 3) arXiv -> 4) OpenAlex search (sin DOI)
    #    Cada etapa solo se consulta si la anterior no produjo un PDF válido.
    if doi:
        urls, is_oa_unpaywall = fuente_unpaywall(doi)
        ok = intentar([("unpaywall", u) for u in urls])
        if not ok:
            ok = intentar([("openalex", u) for u in fuente_openalex_doi(doi)])
    if not ok:
        ok = intentar([("arxiv", u) for u in fuente_arxiv(titulo)])
    if not ok and not doi:
        ok = intentar([("openalex_search", u) for u in fuente_openalex_search(row)])

    if ok:
        base.update(estado="conseguido", fuente=ok[0], url_pdf=ok[1],
                    archivo_local=str(archivo), motivo_fallo="")
    elif not hubo_candidatos:
        if not doi:
            base["motivo_fallo"] = "sin_doi"
        elif is_oa_unpaywall is False:
            base["motivo_fallo"] = "paywall"
        else:
            base["motivo_fallo"] = "no_encontrado"
    else:
        base["motivo_fallo"] = "error_descarga"
        base["fuente"] = ultimo_lote[0][0]
        base["url_pdf"] = ultimo_lote[0][1]

    cp.write_text(json.dumps(base, ensure_ascii=False, indent=1), encoding="utf-8")
    return base

# ----------------------------------------------------------------------------
# Verificación final: 3 PDFs al azar, título extraído vs CSV
# ----------------------------------------------------------------------------
def extraer_texto_pdf(pdf: Path) -> str:
    if shutil.which("pdftotext"):
        try:
            out = subprocess.run(["pdftotext", "-f", "1", "-l", "2", str(pdf), "-"],
                                 capture_output=True, text=True, timeout=60)
            return out.stdout
        except Exception:
            return ""
    try:
        from pypdf import PdfReader
        r = PdfReader(str(pdf))
        return "\n".join((p.extract_text() or "") for p in r.pages[:2])
    except Exception:
        return ""


def verificar(conseguidos, n=3):
    import random
    muestra = random.sample(conseguidos, min(n, len(conseguidos)))
    resultados = []
    for reg in muestra:
        pdf = Path(reg["archivo_local"])
        txt = norm_title(extraer_texto_pdf(pdf))
        objetivo = norm_title(reg["titulo"])
        palabras = [w for w in objetivo.split() if len(w) > 3]
        hits = sum(1 for w in palabras if w in txt)
        coincide = bool(palabras) and hits / len(palabras) >= 0.6
        resultados.append((reg, coincide, f"{hits}/{len(palabras)} palabras clave"))
    return resultados

# ----------------------------------------------------------------------------
# Reportes
# ----------------------------------------------------------------------------
CAMPOS = ["itemID", "primer_autor", "año", "titulo", "DOI", "estado",
          "fuente", "url_pdf", "archivo_local", "motivo_fallo"]


def escribir_reportes(registros, verificacion):
    with open(REPORTE_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        for r in sorted(registros, key=lambda x: x["itemID"]):
            w.writerow({k: r.get(k, "") for k in CAMPOS})

    total = len(registros)
    ok = [r for r in registros if r["estado"] == "conseguido"]
    mal = [r for r in registros if r["estado"] != "conseguido"]
    por_fuente, por_motivo = {}, {}
    for r in ok:
        por_fuente[r["fuente"]] = por_fuente.get(r["fuente"], 0) + 1
    for r in mal:
        por_motivo[r["motivo_fallo"]] = por_motivo.get(r["motivo_fallo"], 0) + 1

    L = []
    L.append("# Reporte de recuperación de PDFs — Biblioteca Zotero\n")
    L.append(f"- Total de registros: **{total}**")
    L.append(f"- Conseguidos: **{len(ok)}**")
    L.append(f"- No conseguidos: **{len(mal)}**")
    tasa = (100.0 * len(ok) / total) if total else 0.0
    L.append(f"- Tasa de éxito: **{tasa:.1f}%**\n")
    L.append("## Desglose por fuente\n")
    for k, v in sorted(por_fuente.items(), key=lambda x: -x[1]):
        L.append(f"- {k}: {v}")
    L.append("\n## No conseguidos por motivo\n")
    for k, v in sorted(por_motivo.items(), key=lambda x: -x[1]):
        L.append(f"- {k}: {v}")

    L.append("\n## PDFs conseguidos\n")
    L.append("| Autor | Año | Título | Fuente |")
    L.append("|---|---|---|---|")
    for r in sorted(ok, key=lambda x: (x["primer_autor"], x["año"])):
        t = r["titulo"].replace("|", "\\|")
        L.append(f"| {r['primer_autor']} | {r['año']} | {t} | {r['fuente']} |")

    L.append("\n## No conseguidos (agrupados por motivo)\n")
    for motivo in sorted(por_motivo):
        L.append(f"\n### {motivo}\n")
        for r in mal:
            if r["motivo_fallo"] == motivo:
                L.append(f"- [{r['itemID']}] {r['primer_autor']} ({r['año']}): {r['titulo']}")

    L.append("\n## Verificación de integridad (3 PDFs al azar)\n")
    if verificacion:
        for reg, coincide, detalle in verificacion:
            marca = "OK ✔" if coincide else "FALLA ✘"
            L.append(f"- {marca} — `{Path(reg['archivo_local']).name}` — "
                     f"título CSV: \"{reg['titulo'][:90]}\" ({detalle})")
    else:
        L.append("- No hubo PDFs conseguidos para verificar.")
    L.append("")
    REPORTE_MD.write_text("\n".join(L), encoding="utf-8")

    return len(ok), total, por_fuente, por_motivo

# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def main():
    workers = MAX_WORKERS_DEFAULT
    if "--workers" in sys.argv:
        workers = int(sys.argv[sys.argv.index("--workers") + 1])

    for d in (DIR_PDF, DIR_CKPT):
        d.mkdir(parents=True, exist_ok=True)

    with open(CSV_IN, newline="", encoding="utf-8-sig") as f:
        filas = list(csv.DictReader(f))
    print(f"Registros en {CSV_IN.name}: {len(filas)}")

    registros, hechos = [], 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(procesar, r): r for r in filas}
        for fut in as_completed(futs):
            reg = fut.result()
            registros.append(reg)
            hechos += 1
            marca = "OK" if reg["estado"] == "conseguido" else f"-- ({reg['motivo_fallo']})"
            print(f"[{hechos:3d}/{len(filas)}] {marca:22s} {reg['titulo'][:70]}")

    conseg = [r for r in registros if r["estado"] == "conseguido"]
    verif = verificar(conseg) if conseg else []
    n_ok, total, por_fuente, por_motivo = escribir_reportes(registros, verif)

    print("\n================ RESUMEN ================")
    print(f"Conseguidos {n_ok}/{total}")
    print("Por fuente:", json.dumps(por_fuente, ensure_ascii=False))
    print("Por motivo de fallo:", json.dumps(por_motivo, ensure_ascii=False))
    print(f"PDFs:      {DIR_PDF}")
    print(f"Reporte:   {REPORTE_CSV}")
    print(f"Resumen:   {REPORTE_MD}")


if __name__ == "__main__":
    main()
