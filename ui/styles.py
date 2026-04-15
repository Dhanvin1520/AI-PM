import streamlit as st


def apply_custom_styles():
    st.markdown(
        """
        <style>
        /* ── Font ─────────────────────────────────────────────────── */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        /* ── Reset ────────────────────────────────────────────────── */
        *, *::before, *::after { box-sizing: border-box; }

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif !important;
            color: #0f172a !important;
        }

        /* ── Remove Streamlit chrome ──────────────────────────────── */
        header[data-testid="stHeader"]  { display: none !important; }
        #MainMenu                       { display: none !important; }
        footer                          { display: none !important; }

        /* ── App background – white everywhere ────────────────────── */
        .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewBlockContainer"],
        [data-testid="stMain"],
        .main,
        .block-container,
        section.main > div {
            background-color: #f8fafc !important;
            background-image: none !important;
        }

        /* ── Page container ───────────────────────────────────────── */
        .block-container {
            max-width: 1320px !important;
            padding: 2rem 2.5rem 4rem !important;
            margin: 0 auto !important;
        }

        /* ── Hero ─────────────────────────────────────────────────── */
        .hero-section {
            background: linear-gradient(135deg, #0284c7 0%, #0ea5e9 60%, #38bdf8 100%);
            border-radius: 14px;
            padding: 2.75rem 2.5rem;
            margin-bottom: 1.75rem;
            text-align: center;
        }
        .hero-badge {
            display: inline-block;
            background: rgba(255,255,255,0.18);
            color: #ffffff;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            border-radius: 100px;
            padding: 4px 14px;
            margin-bottom: 0.9rem;
        }
        .title-main {
            font-size: 2rem !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            margin: 0 0 0.55rem !important;
            line-height: 1.2 !important;
        }
        .subtitle {
            font-size: 1rem !important;
            color: rgba(255,255,255,0.88) !important;
            margin: 0 !important;
        }

        /* ── Step row ─────────────────────────────────────────────── */
        .steps-row {
            display: flex;
            align-items: center;
            gap: 0;
            margin-bottom: 1.75rem;
        }
        .step-chip {
            background: #ffffff;
            border: 1.5px solid #e2e8f0;
            border-radius: 100px;
            padding: 6px 18px;
            font-size: 0.78rem;
            font-weight: 600;
            color: #94a3b8;
            white-space: nowrap;
        }
        .step-chip.active {
            background: #0ea5e9;
            border-color: #0ea5e9;
            color: #ffffff;
        }
        .step-divider {
            flex: 1;
            height: 1.5px;
            background: #e2e8f0;
            min-width: 20px;
        }

        /* ── Section label ────────────────────────────────────────── */
        .section-label {
            font-size: 0.72rem !important;
            font-weight: 600 !important;
            color: #0ea5e9 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.09em !important;
            margin-bottom: 0.5rem !important;
        }

        /* ── File uploader – white, no dark overlay ───────────────── */
        [data-testid="stFileUploader"],
        [data-testid="stFileUploader"] > div,
        [data-testid="stFileUploader"] section,
        [data-testid="stFileUploader"] div {
            background-color: #ffffff !important;
            background: #ffffff !important;
        }
        [data-testid="stFileUploader"] section {
            border: 2px dashed #bae6fd !important;
            border-radius: 12px !important;
            padding: 1.5rem !important;
            background-color: #ffffff !important;
        }
        [data-testid="stFileDropzoneInstructions"],
        [data-testid="stFileUploader"] p,
        [data-testid="stFileUploader"] span,
        [data-testid="stFileUploader"] small {
            color: #64748b !important;
        }
        [data-testid="stFileUploader"] button {
            background-color: #f1f5f9 !important;
            color: #334155 !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 7px !important;
            font-size: 0.85rem !important;
        }

        /* ── Text input – white ───────────────────────────────────── */
        [data-testid="stTextInput"] > div,
        [data-testid="stTextInput"] > div > div {
            background-color: #ffffff !important;
        }
        [data-testid="stTextInput"] input,
        .stTextInput input {
            background-color: #ffffff !important;
            color: #0f172a !important;
            border: 1.5px solid #cbd5e1 !important;
            border-radius: 8px !important;
            padding: 0.65rem 1rem !important;
            font-size: 0.93rem !important;
        }
        [data-testid="stTextInput"] input:focus {
            border-color: #0ea5e9 !important;
            box-shadow: 0 0 0 3px rgba(14,165,233,0.15) !important;
            outline: none !important;
        }
        [data-testid="stTextInput"] input::placeholder {
            color: #94a3b8 !important;
        }

        /* ── Expander – white bg, visible dark text ───────────────── */
        [data-testid="stExpander"],
        details[data-testid="stExpander"] {
            background-color: #ffffff !important;
            border: 1.5px solid #e2e8f0 !important;
            border-radius: 10px !important;
            overflow: hidden !important;
        }
        details[data-testid="stExpander"] > summary {
            background-color: #ffffff !important;
            color: #0f172a !important;
            font-weight: 500 !important;
            font-size: 0.9rem !important;
            padding: 0.8rem 1rem !important;
            cursor: pointer !important;
        }
        details[data-testid="stExpander"] > summary:hover {
            background-color: #f8fafc !important;
        }
        /* The content div inside expander */
        details[data-testid="stExpander"] > div,
        details[data-testid="stExpander"] > div > div,
        details[data-testid="stExpander"] > div > div > div {
            background-color: #ffffff !important;
        }
        /* All text inside expander */
        details[data-testid="stExpander"] p,
        details[data-testid="stExpander"] li,
        details[data-testid="stExpander"] span,
        details[data-testid="stExpander"] div {
            color: #334155 !important;
        }
        details[data-testid="stExpander"] summary svg {
            fill: #0ea5e9 !important;
        }

        /* ── Expander inner custom layout ─────────────────────────── */
        .expander-content {
            display: flex;
            flex-direction: column;
            gap: 12px;
            padding: 4px 0 8px;
        }
        .exp-step {
            display: flex;
            align-items: flex-start;
            gap: 12px;
        }
        .exp-num {
            min-width: 24px;
            height: 24px;
            background: #0ea5e9;
            color: #ffffff !important;
            border-radius: 50%;
            font-size: 0.72rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            margin-top: 1px;
        }
        .exp-text {
            font-size: 0.87rem !important;
            line-height: 1.55 !important;
            color: #334155 !important;
        }

        /* ── Generate button ──────────────────────────────────────── */
        .stButton > button {
            background: linear-gradient(90deg, #0284c7, #0ea5e9) !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.72rem 1.5rem !important;
            font-size: 0.95rem !important;
            font-weight: 600 !important;
            width: 100% !important;
            transition: opacity 0.2s, transform 0.1s !important;
            letter-spacing: 0.01em !important;
        }
        .stButton > button:hover  { opacity: 0.9  !important; transform: translateY(-1px) !important; }
        .stButton > button:active { transform: translateY(0)  !important; }

        /* ── Section divider ──────────────────────────────────────── */
        hr.section-hr {
            border: none !important;
            border-top: 1.5px solid #e2e8f0 !important;
            margin: 0 0 1.25rem !important;
        }

        /* ── Results heading ──────────────────────────────────────── */
        .results-heading {
            margin: 0 !important;
            font-size: 1.35rem !important;
            color: #0f172a !important;
            font-weight: 700 !important;
        }

        /* ── Download button ──────────────────────────────────────── */
        a.download-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 24px;
            background: #0f172a;
            color: #ffffff !important;
            padding: 0.7rem 1.25rem;
            border-radius: 8px;
            text-align: center;
            font-weight: 600;
            font-size: 0.88rem;
            text-decoration: none;
            transition: background 0.2s;
            white-space: nowrap;
        }
        a.download-btn:hover { background: #1e293b; }

        /* ── Metric cards ─────────────────────────────────────────── */
        .metric-card {
            background: #ffffff;
            border: 1.5px solid #e2e8f0;
            border-radius: 12px;
            padding: 1.1rem 1.25rem;
            text-align: left;
        }
        .metric-label {
            font-size: 0.73rem;
            font-weight: 600;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.07em;
            margin-bottom: 6px;
        }
        .metric-value {
            font-size: 1.7rem;
            font-weight: 700;
            color: #0f172a;
            line-height: 1;
            margin-bottom: 6px;
        }
        .metric-delta {
            font-size: 0.78rem;
            font-weight: 500;
        }

        /* ── Change summary cards ─────────────────────────────────── */
        .change-card {
            background: #f0f9ff;
            border: 1.5px solid #bae6fd;
            border-radius: 10px;
            padding: 1rem 1.1rem;
        }
        .change-title {
            font-size: 0.82rem;
            font-weight: 700;
            color: #0284c7;
            margin-bottom: 5px;
        }
        .change-desc {
            font-size: 0.82rem;
            color: #334155;
            line-height: 1.5;
        }

        /* ── Comparison labels ────────────────────────────────────── */
        .compare-label {
            font-size: 0.78rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.07em;
            padding: 5px 12px;
            border-radius: 6px 6px 0 0;
            display: inline-block;
            margin-bottom: -1px;
        }
        .original-label     { background: #f1f5f9; color: #64748b;  border: 1.5px solid #e2e8f0; border-bottom: none; }
        .personalized-label { background: #e0f2fe; color: #0284c7;  border: 1.5px solid #bae6fd; border-bottom: none; }

        /* ── iFrames ──────────────────────────────────────────────── */
        iframe {
            border-radius: 0 10px 10px 10px !important;
            border: 1.5px solid #e2e8f0 !important;
            width: 100% !important;
            display: block !important;
        }

        /* ── Column gap ───────────────────────────────────────────── */
        [data-testid="stHorizontalBlock"] {
            gap: 1.5rem !important;
            align-items: flex-start !important;
        }

        /* ── Spinner ──────────────────────────────────────────────── */
        [data-testid="stSpinner"] p { color: #0ea5e9 !important; }

        /* ── Error alert ──────────────────────────────────────────── */
        [data-testid="stAlert"] {
            border-radius: 10px !important;
            background-color: #fef2f2 !important;
            border-left: 4px solid #ef4444 !important;
            color: #991b1b !important;
        }

        /* ── Image caption ────────────────────────────────────────── */
        .stImage figcaption, .stImage p {
            color: #94a3b8 !important;
            font-size: 0.78rem !important;
        }

        /* ── Scrollbar styling ────────────────────────────────────── */
        ::-webkit-scrollbar       { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #f1f5f9; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 3px; }

        /* ── Responsive ───────────────────────────────────────────── */
        @media (max-width: 900px) {
            .title-main     { font-size: 1.5rem !important; }
            .hero-section   { padding: 1.75rem 1.25rem; }
            .block-container{ padding: 1rem !important; }
            .steps-row      { flex-wrap: wrap; gap: 6px; }
            .step-divider   { display: none; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )