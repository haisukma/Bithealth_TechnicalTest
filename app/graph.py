from langgraph.graph import StateGraph, END

def build_graph(workflow):
    graph = StateGraph(dict)
    graph.add_node("retrieve", workflow.retrieve)
    graph.add_node("answer", workflow.answer)
    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "answer")
    graph.add_edge("answer", END)
    return graph.compile()
