#!/usr/bin/env python3
"""Markdown -> chunks -> embeddings (Ollama) -> Qdrant. Idempotente."""
import hashlib, logging, sqlite3, uuid
from pathlib import Path
import requests
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

BASE = Path("/mnt/Compartida/Descargas_HDD/tesis-doctorado/biblioteca-local")
MD_DIR, DB = BASE/"ocr_out", BASE/"pipeline.db"
LOG = BASE/"logs"/"indexar.log"
COLLECTION, EMBED_URL, MODELO = "tesis-corpus", "http://localhost:11434/api/embed", "bge-m3"
CHUNK_SIZE, OVERLAP = 1000, 150  # caracteres

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG), logging.StreamHandler()])
log = logging.getLogger("indexar")

def trocear(texto: str):
    """Chunks por bloques respetando párrafos."""
    chunks, actual = [], ""
    for parrafo in texto.split("\n\n"):
        if len(actual) + len(parrafo) > CHUNK_SIZE and actual:
            chunks.append(actual.strip())
            actual = actual[-OVERLAP:] + "\n\n" + parrafo  # solape
        else:
            actual += "\n\n" + parrafo
    if actual.strip():
        chunks.append(actual.strip())
    return chunks

def embed(textos, lote=10):
    """Sub-lotes con reintento para no saturar Ollama en CPU."""
    import time
    vectores = []
    for i in range(0, len(textos), lote):
        sub = textos[i:i+lote]
        sub = [t.strip()[:6000] if t.strip() else "(vacío)" for t in sub]
        sub = [t.strip()[:6000] if t.strip() else "(vacío)" for t in sub]
        for intento in range(3):
            try:
                r = requests.post(EMBED_URL, json={"model": MODELO, "input": sub}, timeout=600)
                r.raise_for_status()
                vectores.extend(r.json()["embeddings"])
                break
            except Exception as e:
                log.warning("Reintento %d en sub-lote %d: %s", intento+1, i, e)
                time.sleep(5)
        else:
            raise RuntimeError(f"Sub-lote {i} falló 3 veces")
        log.info("  embeddings: %d/%d", len(vectores), len(textos))
    return vectores

def main():
    conn = sqlite3.connect(DB)
    conn.execute("""CREATE TABLE IF NOT EXISTS indexed(
        doc_hash TEXT PRIMARY KEY, source TEXT, n_chunks INTEGER,
        ts DATETIME DEFAULT CURRENT_TIMESTAMP)""")
    qc = QdrantClient(url="http://localhost:6333")
    # Dimensión de nomic-embed-text = 768
    if not qc.collection_exists(COLLECTION):
        qc.create_collection(COLLECTION, vectors_config=VectorParams(size=1024, distance=Distance.COSINE))
        log.info("Colección %s creada", COLLECTION)

    for md in sorted(MD_DIR.glob("*.md")):
        texto = md.read_text(encoding="utf-8")
        h = hashlib.sha256(texto.encode()).hexdigest()
        if conn.execute("SELECT 1 FROM indexed WHERE doc_hash=?", (h,)).fetchone():
            log.info("OMITIDO (ya indexado): %s", md.name); continue
        chunks = trocear(texto)
        log.info("Indexando %s: %d chunks", md.name, len(chunks))
        vectores = embed(chunks)  # Ollama acepta lote
        puntos = [PointStruct(id=str(uuid.uuid4()), vector=v,
                    payload={"source": md.name, "chunk_id": i, "text": c})
                  for i, (v, c) in enumerate(zip(vectores, chunks))]
        qc.upsert(COLLECTION, puntos)
        conn.execute("INSERT OR REPLACE INTO indexed(doc_hash,source,n_chunks) VALUES(?,?,?)",
                     (h, md.name, len(chunks)))
        conn.commit()
        log.info("OK %s -> %d vectores", md.name, len(puntos))
    conn.close()
    log.info("Total en colección: %d puntos", qc.count(COLLECTION).count)

if __name__ == "__main__":
    main()
