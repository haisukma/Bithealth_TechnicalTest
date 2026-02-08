from app.services.embedding import EmbeddingService

service = EmbeddingService()

query_embedding = service.embed("machine learning engineer")
doc_embedding = service.embed("AI engineer with python experience")

similarity = sum(q * d for q, d in zip(query_embedding, doc_embedding))

print("Similarity score:", similarity)
