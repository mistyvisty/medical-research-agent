# 🏥 Medical Research Assistant

🔴 **Live App:** [View Dashboard](https://medical-research-agent-3mbhgune6spud5lszhhvqs.streamlit.app)

A multi-agent AI system that researches any medical topic using 3 specialized AI agents working in sequence.

## 🤖 How It Works

Research Agent → Summariser Agent → Fact-Checker Agent

- **Agent 1 - Researcher:** Gathers comprehensive medical information
- **Agent 2 - Summariser:** Converts research into patient-friendly language
- **Agent 3 - Fact-Checker:** Validates claims and flags anything uncertain

## 🛠️ Tech Stack
- LangGraph — agent orchestration
- Groq LLaMA 3.3 70B — LLM backbone
- Streamlit — user interface
- Python — core language
- 🐳 Docker — containerisation

## 🚀 Run Locally
1. Clone the repo
2. Create virtual environment:
   python -m venv venv
   venv\Scripts\activate
3. Install dependencies:
   pip install -r requirements.txt
4. Add your Groq API key in .env file:
   GROQ_API_KEY=your_key_here
5. Run the app:
   streamlit run app.py

## ⚠️ Disclaimer
This tool is for informational purposes only.
Always consult a qualified doctor for medical advice.

## 👩‍💻 Built By
Preeti Bhardwaj — [github.com/mistyvisty](https://github.com/mistyvisty)
