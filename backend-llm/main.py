from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests
from qdrant_client import QdrantClient

app = FastAPI()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")
QDRANT_URL = os.getenv("QDRANT_URL", "http://qdrant:6333")

client = QdrantClient(url=QDRANT_URL)
COLLECTION = "docs"


class DocItem(BaseModel):
    id: int
    text: str


class Query(BaseModel):
    question: str


def embed(text: str):
    payload = {
        "model": "nomic-embed-text",  # лёгкая embedding-модель
        "prompt": text
    }
    r = requests.post(f"{OLLAMA_URL}/api/embeddings", json=payload).json()
    return r["embedding"]


@app.on_event("startup")
def init_collection():
    client.recreate_collection(
        collection_name=COLLECTION,
        vector_size=4096,   # см. размер embedding-модели
        distance="Cosine"
    )


@app.post("/add")
def add_doc(item: DocItem):
    vec = embed(item.text)
    client.upsert(
        collection_name=COLLECTION,
        points=[
            {
                "id": item.id,
                "vector": vec,
                "payload": {"text": item.text}
            }
        ]
    )
    return {"status": "ok"}


@app.post("/ask")
def ask(query: Query):
    q_vec = embed(query.question)
    hits = client.search(
        collection_name=COLLECTION,
        query_vector=q_vec,
        limit=3
    )
    context = "\n\n".join([h.payload["text"] for h in hits])

    prompt = f"""
Context:
{context}
Question: {query.question}
Answer using context.
"""
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
    r = requests.post(f"{OLLAMA_URL}/api/generate", json=payload).json()
    return {"answer": r["response"], "context": context}
