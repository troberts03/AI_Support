# Customer Service AI Playground

An AI-powered customer support playground where multiple large language models (LLMs) act as customer service agents.
Ask a question (orders, refunds, shipping, account help), and see how different AI models respond side-by-side.

This project demonstrates skills in Generative AI, multi-model evaluation, model orchestration, and Streamlit deployment.

## Features

Multi-Model Playground: Runs customer questions through local Ollama models (LLaMA2, Mistral).

Streamlit UI: Side-by-side comparison in an interactive web app.

Consistent Agent Role: All models are prompted to respond as professional customer support agents.

## Quickstart
1. Clone the repo
git clone https://github.com/troberts03/AI_Support.git

    `cd AI_Support`

2. Install dependencies
pip install -r requirements.txt

3. Install and run Ollama (for LLaMA2 & Mistral)

    - Download Ollama: https://ollama.ai

    - Pull models:

        `ollama pull llama2`

        `ollama pull mistral`

    - Start the Ollama server:

        `ollama serve`

4. Run the Streamlit app
streamlit run ai_helper.py

## Example Questions

Try asking:

    “How do I track my order?”

    “What is your refund policy?”

    “Do you ship internationally?”

    “How do I reset my password?”

Each AI model will respond as if it were a real support agent.

## Tech Stack

Streamlit
 – interactive UI

Ollama
 – run LLaMA2 / Mistral locally

## Future Enhancements

Add support for OpenAI GPT, Anthropic Claude, and Google Gemini.

Let users select models dynamically from a sidebar (e.g. toggle Gemini, LLaMA2, Mistral).

Add a rating system to evaluate responses.

Show per-model progress indicators during generation.

Expand to a true RAG system with embeddings and vector search.

## License

MIT License: feel free to fork, adapt, and build on this project.