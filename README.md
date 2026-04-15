# 🎯 Landing Page Personalizer Engine


An AI-powered CRO tool that takes an ad creative and a landing page URL, and returns a personalized version of that page — aligned with the ad's messaging, tone, and offer — without touching any HTML structure or CSS.

---

## 🔗 Live Demo

**[https://gapd4gcnfvp2mfm9lnjxd.streamlit.app/](https://gapd4gcnfvp2mfm9lnjxd.streamlit.app/)**

---

## 🧠 How It Works

```
Ad Creative (Image) ──► OCR Engine ──► Ad Text
                                            │
Landing Page URL ──► Scraper ──► DOM Nodes  │
                                            ▼
                              Groq LLaMA 3.3 70B (CRO Rewrite)
                                            │
                                            ▼
                         Personalized Page (text-only mutation)
```

1. **Ad Ingestion** — User uploads an ad creative image. OCR.space API extracts all visible text, headlines, and CTA copy.
2. **Page Scraping** — The target landing page is fetched and parsed. Conversion-critical nodes (`h1`, `h2`, `h3`, `p`, `a`) are extracted.
3. **AI Rewrite** — Ad text + page elements are sent to Groq's LLaMA 3.3 70B with a CRO-specialist system prompt. The model rewrites each element to match the ad's messaging.
4. **DOM Reassembly** — LLM output is validated as JSON and mapped 1:1 back to original DOM nodes. Only text changes — structure, CSS, images, and scripts are untouched.
5. **Side-by-Side Render** — Original vs. personalized page rendered in Streamlit iframes, with CRO metrics and a downloadable HTML file.

---

## 🛡️ Edge Cases Handled

| Issue | Approach |
|---|---|
| **Broken UI** | LLM never generates HTML/CSS — only replaces text nodes via BeautifulSoup `.string`. Layout is always preserved. |
| **Hallucinations** | Output constrained to strict JSON schema `{id, new_text}`. Invalid responses are rejected; original text is preserved as fallback. |
| **Inconsistent Output** | Regex strips markdown fences before JSON parsing. Failed parses fall back to original content silently. |
| **Random Page Changes** | Fresh scrape on every request. Targets semantic tags, not volatile CSS classes or IDs. |

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| OCR | OCR.space API |
| Scraping | requests + BeautifulSoup4 |
| LLM | Groq — LLaMA 3.3 70B Versatile |
| Deployment | Streamlit Community Cloud |

---

## 🚀 Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/Dhanvin1520/AI-PM.git
cd AI-PM

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your Groq API key
echo "GROQ_API_KEY=your_key_here" > .env

# 4. Run the app
streamlit run app.py
```

---

## ☁️ Deploy to Streamlit Cloud

1. Fork this repo
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect the repo
3. Set `GROQ_API_KEY` under **Settings → Secrets**
4. Deploy — no container setup needed

---

## 📁 Project Structure

```
AI-PM/
├── app.py                  # Main Streamlit app
├── backend/
│   ├── ocr_engine.py       # Ad creative text extraction
│   ├── scraper.py          # Landing page HTML fetcher
│   └── llm_engine.py       # Groq LLM rewrite engine
├── ui/
│   └── styles.py           # Custom CSS styles
├── requirements.txt
└── README.md
```

---

## 📌 Assumptions

- Landing page must be publicly accessible (no login walls)
- Ad creative is provided as an image (JPG/PNG)
- CRO metrics shown are illustrative benchmarks, not real-time computed values
- System modifies text only — image swapping is out of scope for this prototype
