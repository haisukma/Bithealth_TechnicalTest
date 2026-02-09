from pydantic import BaseModel

class QuestionRequest(BaseModel):
    """Request payload for asking a question to the RAG system."""
    question: str

class DocumentRequest(BaseModel):
    text: str
