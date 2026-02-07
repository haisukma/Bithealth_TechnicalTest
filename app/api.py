import time
from fastapi import APIRouter, HTTPException

router = APIRouter()

def register_routes(router, rag_chain, store, embedder):

    @router.post("/ask")
    def ask(req):
        start = time.time()
        try:
            result = rag_chain.invoke({"question": req.question})
            return {
                "question": req.question,
                "answer": result["answer"],
                "context_used": result.get("context", []),
                "latency_sec": round(time.time() - start, 3),
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @router.post("/add")
    def add(req):
        try:
            vector = embedder.embed(req.text)
            doc_id = store.count()
            store.add(doc_id, req.text, vector)
            return {"id": doc_id, "status": "added"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @router.get("/status")
    def status():
        return {
            "docs_count": store.count(),
            "graph_ready": rag_chain is not None,
        }
