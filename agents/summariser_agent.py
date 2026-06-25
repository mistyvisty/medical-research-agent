from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)

SYSTEM = """You are a medical content summariser.
Take detailed research and create a clear, patient-friendly summary.
Structure your output EXACTLY like this:

## Overview
(2-3 sentences explaining what this is)

## Key Facts
- (bullet points of most important information)

## What You Should Know
(practical takeaways for someone reading this)

## When to See a Doctor
(clear guidance on urgency)

Keep language simple. Avoid jargon. Be concise but complete."""

def summarise(state: dict) -> dict:
    research = state["research"]
    messages = [
        SystemMessage(content=SYSTEM),
        HumanMessage(content=f"Summarise this research:\n\n{research}")
    ]
    response = llm.invoke(messages)
    state["summary"] = response.content
    state["status"] = "summarised"
    print("[Summariser Agent] Done")
    return state