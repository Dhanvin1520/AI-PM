import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
        color: #0f172a !important;
    }

    header {display:none;}

    .stApp {
        background: #f8fafc;
    }

    .block-container {
        max-width: 900px;
        margin: auto;
        padding-top: 2rem;
    }

    /* HERO FIXED */
    .hero-section {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 2.5rem;
        text-align: center;
        margin-bottom: 1.5rem;
    }

    .hero-badge {
        background: #f1f5f9;
        color: #0ea5e9;
        font-size: 0.7rem;
        padding: 4px 12px;
        border-radius: 999px;
        display:inline-block;
        margin-bottom:10px;
    }

    .title-main {
        font-size: 1.9rem;
        font-weight: 700;
        color: #0f172a;
    }

    .subtitle {
        color: #64748b;
        font-size: 0.95rem;
    }

    /* UPLOADER FIX */
    [data-testid="stFileUploader"] section {
        border: 2px dashed #e2e8f0 !important;
        border-radius: 12px;
        padding: 1.2rem;
        background: white !important;
    }

    /* INPUT */
    .stTextInput input {
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px;
        padding: 10px;
    }

    /* BUTTON */
    .stButton button {
        background: linear-gradient(90deg, #0284c7, #0ea5e9);
        color: white;
        border-radius: 8px;
        padding: 10px;
        font-weight: 600;
    }

    /* EXPANDER FIX (IMPORTANT) */
    details[data-testid="stExpander"] {
        background: #ffffff !important;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
    }

    details[data-testid="stExpander"] > summary {
        background: #ffffff !important;
        color: #0f172a !important;
    }

    details[data-testid="stExpander"] > div {
        background: transparent !important;
    }

    /* REMOVE OVERLAY ISSUE */
    div[style*="background-color: rgba"] {
        display: none !important;
    }

    </style>
    """, unsafe_allow_html=True)