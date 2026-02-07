from fastapi import FastAPI
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

from app.services.embedding import EmbeddingService
from app.services.rag import RagWorkflow
from app.stores.memory import InMemoryDocumentStore
from app.stores.qdrant import QdrantDocumentStore
from app.graph import build_graph
from app.api import router, register_routes
from app.models import QuestionRequest, DocumentRequest

app = FastAPI(title="Learning RAG Demo")

embedder = EmbeddingService()

try:
    client = QdrantClient("http://localhost:6333")
    if client.collection_exists("demo_collection"):
        client.delete_collection("demo_collection")

    client.create_collection(
        collection_name="demo_collection",
        vectors_config=VectorParams(size=128, distance=Distance.COSINE),
    )
    store = QdrantDocumentStore(client, "demo_collection")
except Exception:
    print("Qdrant not available. Using in-memory store.")
    store = InMemoryDocumentStore()

workflow = RagWorkflow(embedder, store)
chain = build_graph(workflow)

register_routes(router, chain, store, embedder)
app.include_router(router)
