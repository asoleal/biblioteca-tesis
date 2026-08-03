#!/usr/bin/env python3
"""RAG: recupera chunks diversos -> qwen3:4b redacta con citas. Con progreso."""
import sys, time, requests
from qdrant_client import QdrantClient

OLLAMA = "http://localhost:11434"
def log(msg, t0): print(f"[{time.time()-t0:6.1f}s] {msg}", flush=True)

def main():
    t0 = time.time()
    pregunta = " ".join(sys.argv[1:])
    if not pregunta:
        print("Uso: python3 scripts/preguntar.py 'tu pregunta'"); return

    log("Generando embedding de la pregunta...", t0)
    vec = requests.post(f"{OLLAMA}/api/embed",
        json={"model": "bge-m3", "input": pregunta}, timeout=120).json()["embeddings"][0]

    log("Buscando en Qdrant (top-12 -> 5 diversos)...", t0)
    qc = QdrantClient(url="http://localhost:6333")
    candidatos = qc.query_points("tesis-corpus", query=vec, limit=12).points
    hits, por_doc = [], {}
    for h in candidatos:
        src = h.payload["source"]
        if por_doc.get(src, 0) < 2:
            hits.append(h); por_doc[src] = por_doc.get(src, 0) + 1
        if len(hits) == 5: break
    log(f"Recuperados {len(hits)} chunks de {len(por_doc)} papers", t0)

    contexto = "\n\n".join(
        f"[FUENTE {i+1}: {h.payload['source']}]\n{h.payload['text'][:800]}"
        for i, h in enumerate(hits))
    prompt = f"""Eres un asistente de investigación doctoral. Responde en español
basándote SOLO en el contexto. Cita como [FUENTE n] cada afirmación.
Si el contexto no alcanza, dilo explícitamente.

CONTEXTO:
{contexto}

PREGUNTA: {pregunta}

RESPUESTA (máx 200 palabras): /no_think"""

    log("qwen2.5 redactando (etapa lenta, 2-5 min en CPU)...", t0)
    r = requests.post(f"{OLLAMA}/api/generate",
        json={"model": "qwen2.5:7b-instruct", "prompt": prompt, "stream": False,
              "think": False,
              "options": {"num_ctx": 8192}}, timeout=900)
    log("Respuesta lista", t0)

    respuesta = r.json()["response"]
    print("=" * 70)
    print(respuesta.replace("<think>", "").split("</think>")[-1].strip())
    print("=" * 70)
    print("\nFUENTES:")
    for i, h in enumerate(hits, 1):
        print(f"  [{i}] {h.payload['source']} (score={h.score:.3f})")

if __name__ == "__main__":
    main()
