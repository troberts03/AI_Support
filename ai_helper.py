import streamlit as st
import ollama
from dotenv import load_dotenv

load_dotenv()

# -------------------------------
# Generative AI
# -------------------------------
# def call_openai(user_q: str, context: str) -> str:
#     # Example: integrate with paid OpenAI API
#     return f"[OpenAI GPT] I think the answer is: {context}"

# def call_claude(user_q: str, context: str) -> str:
#     # Example: integrate with paid Anthropic API
#     return f"[Claude] Based on context, here’s what I’d suggest: {context}"

# def call_gemini(user_q: str, context: str) -> str:
#       Example: requires paid Gemini API
#     return f"[Gemini] Based on context, here’s what I’d suggest: {context}"

def call_ollama(user_q: str, context: str, model: str = "llama2") -> str:
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful customer support assistant. Always answer in a professional, empathetic way."},
                {"role": "user", "content": f"Customer question: {user_q}\nContext: {context}"}
            ]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Ollama {model} error: {e}"

# -------------------------------
# Hybrid Answering
# -------------------------------
def get_answers(user_q: str) -> dict:

    # Context for LLM fallback
    context = (
        "This is a customer service scenario. Provide answers about orders, refunds, "
        "shipping, and account management in a professional support tone."
    )

    answers = {}

    # Call multiple models for comparison
    # answers["OpenAI GPT"]: call_openai(user_q, context),
    # answers["Claude"]: call_claude(user_q, context),
    # answers["Gemini"] = call_gemini(user_q, context)
    answers["Ollama LLaMA2"] = call_ollama(user_q, context, model="llama2")
    answers["Ollama Mistral"] = call_ollama(user_q, context, model="mistral")

    return answers

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Customer Service AI Playground", layout="wide")
st.title("Customer Service AI Playground")

st.markdown(
    "Ask a **customer service question** (order, refund, shipping, account help) "
    "and compare how different AI models respond as if they were real support agents."
)

# Session state for button disabling
if "loading" not in st.session_state:
    st.session_state.loading = False

question = st.text_input("Your question")

# Ask button with disabled state
ask_button = st.button("Ask", disabled=st.session_state.loading)

if ask_button and question.strip():
    st.session_state.loading = True
    with st.spinner("Thinking... contacting support agents..."):
        answers = get_answers(question)

    st.markdown(f"**You:** {question}")

    cols = st.columns(len(answers))
    for i, (model, response) in enumerate(answers.items()):
        with cols[i]:
            st.subheader(model)
            st.markdown(response)

    st.session_state.loading = False
