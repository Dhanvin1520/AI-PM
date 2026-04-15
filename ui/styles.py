import streamlit as st


def apply_custom_styles():
    st.markdown(
        """
        <style>
        /* ── Google Font ──────────────────────────────────────────── */
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

        /* ── Global reset ─────────────────────────────────────────── */
        *, *::before, *::after { box-sizing: border-box; }

        html, body, [class*="css"] {
            font-family: 'DM Sans', sans-serif !important;
            color: #111827 !important;
        }

        /* ── Remove Streamlit chrome ──────────────────────────────── */
        header[data-testid="stHeader"]        { display: none !important; }
        #MainMenu                             { display: none !important; }
        footer                                { display: none !important; }
        .viewerBadge_container__1QSob         { display: none !important; }

        /* ── App background — pure white ──────────────────────────── */
        .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewBlockContainer"],
        .main,
        .block-container {
            background-color: #ffffff !important;
            background-image: none !important;
        }

        /* ── Page width & padding ─────────────────────────────────── */
        .block-container {
            max-width: 1280px !important;
            padding: 2rem 2rem 4rem !important;
            margin: 0 auto !important;
        }

        /* ── Hero section ─────────────────────────────────────────── */
        .hero-section {
            background: linear-gradient(135deg, #4f46e5 0%, #6366f1 50%, #818cf8 100%);
            border-radius: 16px;
            padding: 2.5rem 2rem;
            margin-bottom: 2rem;
            text-align: center;
        }
        .title-main {
            font-size: 2rem !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            margin: 0 0 0.5rem !important;
        }
        .subtitle {
            font-size: 1rem !important;
            color: rgba(255,255,255,0.88) !important;
            margin: 0 !important;
        }

        /* ── Section labels ───────────────────────────────────────── */
        .section-label {
            font-size: 0.85rem !important;
            font-weight: 600 !important;
            color: #4f46e5 !important;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.4rem !important;
        }

        /* ── File uploader — white background ─────────────────────── */
        [data-testid="stFileUploader"],
        [data-testid="stFileUploader"] > div,
        [data-testid="stFileUploader"] section {
            background-color: #ffffff !important;
            background: #ffffff !important;
        }
        [data-testid="stFileUploader"] section {
            border: 2px dashed #d1d5db !important;
            border-radius: 12px !important;
            padding: 1.5rem !important;
            background-color: #ffffff !important;
        }
        [data-testid="stFileDropzoneInstructions"],
        [data-testid="stFileUploader"] p,
        [data-testid="stFileUploader"] span,
        [data-testid="stFileUploader"] small {
            color: #6b7280 !important;
        }
        /* The "Browse files" button inside uploader */
        [data-testid="stFileUploader"] button {
            background-color: #f3f4f6 !important;
            color: #374151 !important;
            border: 1px solid #d1d5db !important;
            border-radius: 6px !important;
        }

        /* ── Text input — white background ────────────────────────── */
        [data-testid="stTextInput"] input,
        .stTextInput input {
            background-color: #ffffff !important;
            color: #111827 !important;
            border: 1.5px solid #d1d5db !important;
            border-radius: 8px !important;
            padding: 0.6rem 0.9rem !important;
            font-size: 0.95rem !important;
        }
        [data-testid="stTextInput"] input:focus {
            border-color: #4f46e5 !important;
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15) !important;
            outline: none !important;
        }
        [data-testid="stTextInput"] input::placeholder {
            color: #9ca3af !important;
        }

        /* ── Expander — white background, white interior ──────────── */
        [data-testid="stExpander"],
        details[data-testid="stExpander"] {
            background-color: #ffffff !important;
            border: 1px solid #e5e7eb !important;
            border-radius: 10px !important;
        }
        details[data-testid="stExpander"] summary {
            background-color: #ffffff !important;
            color: #374151 !important;
            font-weight: 500 !important;
            padding: 0.75rem 1rem !important;
        }
        details[data-testid="stExpander"] > div {
            background-color: #ffffff !important;
            padding: 0.5rem 1rem 1rem !important;
        }
        details[data-testid="stExpander"] p,
        details[data-testid="stExpander"] li,
        details[data-testid="stExpander"] span {
            color: #374151 !important;
        }
        /* Chevron icon */
        details[data-testid="stExpander"] summary svg {
            fill: #4f46e5 !important;
        }

        /* ── Generate button ──────────────────────────────────────── */
        .stButton > button {
            background: linear-gradient(90deg, #4f46e5, #6366f1) !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.75rem 1.5rem !important;
            font-size: 1rem !important;
            font-weight: 600 !important;
            width: 100% !important;
            cursor: pointer !important;
            transition: opacity 0.2s ease, transform 0.1s ease !important;
        }
        .stButton > button:hover  { opacity: 0.9  !important; transform: translateY(-1px) !important; }
        .stButton > button:active { transform: translateY(0)  !important; }

        /* ── Download button ──────────────────────────────────────── */
        a.download-btn {
            display: block;
            background: linear-gradient(90deg, #059669, #10b981);
            color: #ffffff !important;
            padding: 0.75rem 1.5rem;
            border-radius: 10px;
            text-align: center;
            font-weight: 600;
            font-size: 1rem;
            text-decoration: none;
            transition: opacity 0.2s ease;
        }
        a.download-btn:hover { opacity: 0.88; }

        /* ── iFrames (comparison panels) — full width, no scrollbar bleed ── */
        iframe {
            border-radius: 10px !important;
            border: 1px solid #e5e7eb !important;
            width: 100% !important;
        }

        /* ── Columns gap fix ──────────────────────────────────────── */
        [data-testid="stHorizontalBlock"] {
            gap: 1.25rem !important;
            align-items: flex-start !important;
        }

        /* ── Divider ──────────────────────────────────────────────── */
        hr { border-color: #e5e7eb !important; margin: 1.5rem 0 !important; }

        /* ── Spinner text ─────────────────────────────────────────── */
        [data-testid="stSpinner"] p { color: #4f46e5 !important; }

        /* ── Error / info boxes ───────────────────────────────────── */
        [data-testid="stAlert"] {
            border-radius: 10px !important;
            background-color: #fef2f2 !important;
            border-left: 4px solid #ef4444 !important;
            color: #991b1b !important;
        }

        /* ── Image caption ────────────────────────────────────────── */
        .stImage p { color: #6b7280 !important; font-size: 0.82rem !important; }

        /* ── Responsive: stack columns on small screens ───────────── */
        @media (max-width: 768px) {
            .title-main  { font-size: 1.4rem !important; }
            .hero-section { padding: 1.5rem 1rem; }
            .block-container { padding: 1rem !important; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )