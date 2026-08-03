#!/usr/bin/env python3
"""Consulta semántica sobre tesis-corpus."""
import sys, requests
from qdrant_client import QdrantClient

pregunta = " ".join(sys.argv[1:]) or "cinética de crecimiento de larvas"
vec = requests.post("http://localhost:11434/api/embed",
    json={"model": "bge-m3", "input": pregunta}, timeout=120
).json()["embeddings"][0]

qc = QdrantClient(url="http://localhost:6333")
hits = qc.query_points("tesis-corpus", query=vec, limit=3).points
for i, h in enumerate(hits, 1):
    print(f"\n=== [{i}] score={h.score:.3f} | {h.payload['source']} chunk {h.payload['chunk_id']} ===")
    print(h.payload["text"][:400])
