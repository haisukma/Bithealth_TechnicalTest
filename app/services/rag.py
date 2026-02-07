class RagWorkflow:
    def __init__(self, embedder, store):
        self.embedder = embedder
        self.store = store

    def retrieve(self, state: dict) -> dict:
        query = state["question"]
        vector = self.embedder.embed(query)
        context = self.store.search(query, vector)
        state["context"] = context
        return state

    def answer(self, state: dict) -> dict:
        ctx = state.get("context", [])
        if ctx:
            state["answer"] = f"I found this: '{ctx[0][:100]}...'"
        else:
            state["answer"] = "Sorry, I don't know."
        return state
