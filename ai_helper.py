import streamlit as st
import re

FAQ = [
    {
        "q": "What does the eligibility verification agent (EVA) do?",
        "a": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
    },
    {
        "q": "What does the claims processing agent (CAM) do?",
        "a": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
    },
    {
        "q": "How does the payment posting agent (PHIL) work?",
        "a": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
    },
    {
        "q": "Tell me about Thoughtful AI's Agents.",
        "a": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
    },
    {
        "q": "What are the benefits of using Thoughtful AI's agents?",
        "a": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
    }
]

def clean(s: str) -> list[str]:
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s]+", " ", s)
    return [w for w in s.split() if w]

def score(user_q: str, kb_q: str) -> int:
    u = set(clean(user_q))
    k = set(clean(kb_q))
    return len(u & k)

def get_answer(user_q: str) -> str:
    best = None
    best_score = -1
    for item in FAQ:
        s = score(user_q, item["q"])
        if s > best_score:
            best_score = s
            best = item
    if best and best_score > 0:
        return best["a"]
    return (
        "I couldn't find a direct match in the Thoughtful AI FAQ.\n"
        "Thoughtful AI builds automation agents for healthcare RCM like eligibility (EVA), claims (CAM), "
        "and payment posting (PHIL). Rephrase with the agent name for a more precise answer."
    )

st.set_page_config(page_title="Thoughtful AI Support")
st.title("Thoughtful AI: Support Agent")

question = st.text_input("Ask a question about Thoughtful AI:")
if st.button("Ask") and question.strip():
    answer = get_answer(question)
    st.markdown(f"**You:** {question}")
    st.markdown(f"**Agent:** {answer}")
elif question.strip():
    answer = get_answer(question)
    st.markdown(f"**You:** {question}")
    st.markdown(f"**Agent:** {answer}")
