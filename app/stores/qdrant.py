from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

class QdrantDocumentStore:
    def __init__(self, client: QdrantClient, collection_name: str):
        self.client = client
        self.collection = collection_name

    def add(self, doc_id: int, text: str, vector: list[float]):
        self.client.upsert(
            collection_name=self.collection,
            points=[
                PointStruct(
                    id=doc_id,
                    vector=vector,
                    payload={"text": text}
                )
            ]
        )

    def search(self, query: str, vector: list[float], limit: int = 2) -> list[str]:
        hits = self.client.search(
            collection_name=self.collection,
            query_vector=vector,
            limit=limit
        )
        return [h.payload["text"] for h in hits]

    def count(self) -> int:
        info = self.client.get_collection(self.collection)
        return info.points_count or 0
