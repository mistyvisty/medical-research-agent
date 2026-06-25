from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)

SYSTEM = """You are a medical research specialist.
Given a health topic, gather comprehensive information:
- What the condition/topic is
- Causes and risk factors
- Symptoms and diagnosis
- Current treatments and research
- Reliable statistics and data
Be thorough, factual, and cite what type of sources would verify this."""

def research(state: dict) -> dict:
    topic = state["topic"]
    messages = [
        SystemMessage(content=SYSTEM),
        HumanMessage(content=f"Research this medical topic thoroughly: {topic}")
    ]
    response = llm.invoke(messages)
    state["research"] = response.content
    state["status"] = "researched"
    print(f"[Research Agent] Done for topic: {topic}")
    return state