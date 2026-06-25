import streamlit as st
from graph import build_graph

st.set_page_config(
    page_title="Medical Research Assistant",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Medical Research Assistant")
st.caption("Powered by 3 AI agents: Researcher → Summariser → Fact-Checker")

with st.sidebar:
    st.header("How it works")
    st.markdown("""
    **Agent 1 — Researcher**  
    Gathers comprehensive information on your topic

    **Agent 2 — Summariser**  
    Condenses into clear, patient-friendly language

    **Agent 3 — Fact-Checker**  
    Validates claims and flags anything uncertain
    """)
    st.divider()
    st.caption("Always consult a qualified doctor for medical advice.")

topic = st.text_input(
    "Enter a medical topic to research:",
    placeholder="e.g. PCOS, Type 2 Diabetes, Migraine, Anxiety..."
)

if st.button("Research →", type="primary") and topic:
    graph = build_graph()

    col1, col2 = st.columns(2)

    with st.status("Running agents...", expanded=True) as status:
        st.write("Agent 1: Researching...")
        result = graph.invoke({
            "topic": topic,
            "research": "",
            "summary": "",
            "factcheck": "",
            "status": "starting"
        })
        st.write("Agent 2: Summarising...")
        st.write("Agent 3: Fact-checking...")
        status.update(label="Complete!", state="complete")

    with col1:
        st.subheader("Summary")
        st.markdown(result["summary"])

    with col2:
        st.subheader("Fact-Check Report")
        st.markdown(result["factcheck"])

    with st.expander("View full research (raw)"):
        st.markdown(result["research"])