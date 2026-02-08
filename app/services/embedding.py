import random

class EmbeddingService:
    def __init__(self, dim: int = 128):
        self._dim = dim

    def embed(self, text: str) -> list[float]:
        rng = random.Random(abs(hash(text)) % 10000)
        return [rng.random() for _ in range(self._dim)]
