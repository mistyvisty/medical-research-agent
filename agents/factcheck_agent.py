from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.1
)

SYSTEM = """You are a medical fact-checking specialist.
Review the research and summary for accuracy. Your job:

1. VERIFY: Identify claims that are well-established medical consensus
2. FLAG: Mark any claims that are contested, outdated, or need verification
3. ADD: Note any important information that was missed
4. WARN: Add a disclaimer about consulting real doctors

Output format:
## Fact-Check Report

### Verified Claims
(list what is accurate)

### Claims to Verify
(list anything uncertain with why)

### Missing Important Info
(anything critical that was left out)

### Medical Disclaimer
(always include a proper disclaimer)"""

def factcheck(state: dict) -> dict:
    research = state["research"]
    summary = state["summary"]
    messages = [
        SystemMessage(content=SYSTEM),
        HumanMessage(content=f"""
Research:\n{research}

Summary:\n{summary}

Please fact-check both of the above.""")
    ]
    response = llm.invoke(messages)
    state["factcheck"] = response.content
    state["status"] = "complete"
    print("[Fact-Check Agent] Done")
    return state