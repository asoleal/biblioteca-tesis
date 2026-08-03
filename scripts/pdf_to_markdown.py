#!/usr/bin/env python3
"""PDF -> Markdown HÍBRIDO: PyMuPDF (rápido) o Docling (escaneos). Idempotente."""
import hashlib, logging, sqlite3, sys
from pathlib import Path

BASE = Path("/mnt/Compartida/Descargas_HDD/tesis-doctorado/biblioteca-local")
PDFS, OUT, DB = BASE/"pdfs", BASE/"ocr_out", BASE/"pipeline.db"
LOG = BASE/"logs"/"pdf_to_markdown.log"
MIN_CHARS_PAG = 150  # si el PDF da menos que esto por página, es escaneo -> Docling

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG), logging.StreamHandler()])
log = logging.getLogger("pdf2md")

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def via_pymupdf(pdf: Path):
    """Extracción directa. Devuelve texto o None si parece escaneo."""
    import fitz
    doc = fitz.open(str(pdf))
    partes = [pag.get_text() for pag in doc]
    texto = "\n\n".join(p.strip() for p in partes if p.strip())
    n = max(len(doc), 1)
    doc.close()
    if len(texto) / n < MIN_CHARS_PAG:
        return None
    return texto

def via_docling(pdf: Path) -> str:
    from docling.document_converter import DocumentConverter
    converter = DocumentConverter()
    return converter.convert(str(pdf)).document.export_to_markdown()

def main():
    OUT.mkdir(exist_ok=True); LOG.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB)
    conn.execute("""CREATE TABLE IF NOT EXISTS processed(
        hash TEXT PRIMARY KEY, source TEXT, output TEXT, status TEXT, modo TEXT,
        ts DATETIME DEFAULT CURRENT_TIMESTAMP)""")
    # migración suave: añadir columna modo si la tabla es vieja
    try: conn.execute("ALTER TABLE processed ADD COLUMN modo TEXT")
    except sqlite3.OperationalError: pass
    pdfs = sorted(PDFS.glob("*.pdf"))
    log.info("Encontrados %d PDFs", len(pdfs))
    for pdf in pdfs:
        h = sha256(pdf)
        if conn.execute("SELECT 1 FROM processed WHERE hash=? AND status='ok'", (h,)).fetchone():
            continue
        try:
            md = via_pymupdf(pdf)
            modo = "pymupdf"
            if md is None:
                log.info("Escaneo o poco texto -> Docling: %s", pdf.name)
                md = via_docling(pdf)
                modo = "docling"
            out = OUT / (pdf.stem + ".md")
            out.write_text(md, encoding="utf-8")
            conn.execute("INSERT OR REPLACE INTO processed(hash,source,output,status,modo) VALUES(?,?,?,'ok',?)",
                         (h, pdf.name, out.name, modo))
            conn.commit()
            log.info("OK [%s] -> %s (%d chars)", modo, out.name, len(md))
        except Exception as e:
            conn.execute("INSERT OR REPLACE INTO processed(hash,source,output,status) VALUES(?,?,?,'error')",
                         (h, pdf.name, str(e)))
            conn.commit()
            log.error("FALLO %s: %s", pdf.name, e)
    conn.close()

if __name__ == "__main__":
    sys.exit(main())
