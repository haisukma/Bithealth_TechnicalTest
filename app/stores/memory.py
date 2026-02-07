class InMemoryDocumentStore:
    def __init__(self):
        self._docs: list[str] = []

    def add(self, doc_id: int, text: str, vector: list[float]):
        self._docs.append(text)

    def search(self, query: str, vector: list[float], limit: int = 2) -> list[str]:
        results = [d for d in self._docs if query.lower() in d.lower()]
        if not results and self._docs:
            return [self._docs[0]]
        return results[:limit]

    def count(self) -> int:
        return len(self._docs)
