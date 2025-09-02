Thoughtful AI – Simple Support Agent

A lightweight chatbot built with Streamlit that answers common questions about Thoughtful AI using a small hardcoded FAQ.
If a user’s question doesn’t match, the bot gives a short fallback answer.

Requirements

Python 3.11 (recommended)
streamlit

Setup

Clone or download this project
Put the files in a folder.

Create and activate a virtual environment

python3.11 -m venv venv
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Run the app
streamlit run ai_helper.py

The app will open in your browser.

How it works

FAQ matching: simple keyword overlap against hardcoded Q/A pairs.

Fallback: if no match, gives a short generic Thoughtful AI explanation.

UI: single input box + button; displays the answer.

Example Questions

What does the eligibility verification agent (EVA) do?

What does the claims processing agent (CAM) do?

How does the payment posting agent (PHIL) work?

Tell me about Thoughtful AI's Agents.

What are the benefits of using Thoughtful AI's agents?
