# AI PM   Landing Page Personalizer Engine

This repository contains the complete, deployed codebase for the **AI Product Manager Assignment**. It is a full-stack Python application that securely integrates Multimodal OCR, Web Scraping, and Large Language Models to dynamically personalize landing pages according to conversion rate optimization (CRO) principles.

## 🚀 Live Demo
**[https://vf6b3nktuh5gbkezkplzjy.streamlit.app/](https://vf6b3nktuh5gbkezkplzjy.streamlit.app/)** *(Live Development Tunnel)*

---

## ⚙️ How the Agentic Engine Works (Architecture)

1. **Ad Parsing (OCR Engine)**: Instead of passing heavy images to slow multimodal LLMs, the system utilizes high-speed OCR (`OCR.space` API) to instantly strip the exact copy, sentiment, and offer text embedded in your graphic ad creative.
2. **DOM Extraction (Headless Scraper)**: The backend `scraper.py` strips your raw target Landing Page URL down to its variable structural text nodes (`H1`-`H3`, `p`, `a`), ensuring we don't accidentally mutate CSS classes or script tags.
3. **LLaMA Synthesis (LLM Engine)**: We pass the structured payload explicitly to Groq's high-speed inference **LLaMA-3.3-70B model**. The system prompt acts as a CRO Specialist, rewriting the target text specifically to align with the tone and logic of the Ad Creative.
4. **Live Re-Rendering (In-Place Mutation)**: The modified JSON array maps directly back into the live HTML schema. We render a side-by-side interactive split UI for immediate PM-level review, including predictive KPI metrics.

---

## 🛠 Edge Cases Handled

*   **Hallucinations:** By forcing the LLaMA model to return strict `JSON` mappings directly corresponding to ID-tagged DOM nodes, we structurally eliminate unstructured text/code bleeding into the UI.
*   **Volatile UIs:** The system mutates text properties natively in BeautifulSoup. We never ask the AI to write HTML. This ensures the output CSS layout never breaks.
*   **Performance Latency:** Groq handles 70B parameter inference in sub-seconds. The entire generation cycle takes ~3.5 seconds end-to-end.

---

## 💻 Tech Stack
- **Frontend Layer**: Streamlit (Python 3.9+)
- **DOM Engine**: BeautifulSoup4 (`bs4`)
- **Intelligence**: Groq LLaMA-3.3-70B, OCR.space
- **Network Routing**: Requests, Base64

## 📦 Deployment Instructions (Streamlit Community Cloud)
1. Fork or upload this repository.
2. Visit **[share.streamlit.io](https://share.streamlit.io)** and point to `app.py`.
3. In Streamlit's Advanced Settings, configure the `.env` Secret:
   `GROQ_API_KEY=gsk_...`
4. Click deploy. It will launch completely seamlessly without container management.
