from langgraph.graph import StateGraph, END
from typing import TypedDict
from agents.research_agent import research
from agents.summariser_agent import summarise
from agents.factcheck_agent import factcheck

class AgentState(TypedDict):
    topic: str
    research: str
    summary: str
    factcheck: str
    status: str

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("researcher", research)
    graph.add_node("summariser", summarise)
    graph.add_node("factchecker", factcheck)

    graph.set_entry_point("researcher")
    graph.add_edge("researcher", "summariser")
    graph.add_edge("summariser", "factchecker")
    graph.add_edge("factchecker", END)

    return graph.compile()

if __name__ == "__main__":
    app = build_graph()
    result = app.invoke({
        "topic": "PCOS (Polycystic Ovary Syndrome)",
        "research": "",
        "summary": "",
        "factcheck": "",
        "status": "starting"
    })
    print("\n=== SUMMARY ===")
    print(result["summary"])
    print("\n=== FACT CHECK ===")
    print(result["factcheck"])