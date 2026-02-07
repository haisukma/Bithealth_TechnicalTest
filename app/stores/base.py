from abc import ABC, abstractmethod

class DocumentStore(ABC):

    @abstractmethod
    def add(self, doc_id: int, text: str, vector: list[float]):
        pass

    @abstractmethod
    def search(self, query: str, vector: list[float], limit: int = 2) -> list[str]:
        pass

    @abstractmethod
    def count(self) -> int:
        pass
