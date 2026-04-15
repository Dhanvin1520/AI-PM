import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        .stApp {
            background-color: #f8fafc;
            background-image: radial-gradient(#cbd5e1 1px, transparent 1px);
            background-size: 24px 24px;
            opacity: 1 !important;
        }

        body {
            font-family: 'Inter', sans-serif;
        }

        header {display: none !important;}

        section[data-testid="stAppViewContainer"],
        .block-container,
        .main {
            opacity: 1 !important;
            filter: none !important;
        }

        h1, h2, h3, p, span, div, label {
            color: #0f172a !important;
        }

        .hero-section {
            background: linear-gradient(180deg, #ffffff 0%, rgba(255,255,255,0) 100%);
            padding: 3rem 0 2rem 0;
            margin-top: -4rem;
            margin-bottom: 2rem;
            border-bottom: 1px solid #e2e8f0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        .title-main {
            font-size: 3rem;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 0.5rem;
            text-align: center;
            letter-spacing: -0.04em;
        }

        .subtitle {
            text-align: center;
            color: #64748b;
            font-size: 1.15rem;
            font-weight: 500;
            max-width: 600px;
            margin: 0 auto 2.5rem auto;
            line-height: 1.5;
        }

        .stTextInput > div > div > input {
            background-color: #ffffff !important;
            color: #0f172a !important;
            border: 1px solid #cbd5e1 !important;
            border-radius: 8px;
            padding: 0.85rem 1rem;
            font-size: 1rem;
            box-shadow: 0 1px 2px 0 rgba(15, 23, 42, 0.05);
        }

        .stTextInput > div > div > input:focus {
            border-color: #6366f1 !important;
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2) !important;
        }

        .stButton > button {
            background-color: #4f46e5 !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.75rem 2rem !important;
            font-weight: 600 !important;
            width: 100% !important;
            box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.2);
        }

        .stButton > button:hover {
            background-color: #4338ca !important;
            transform: translateY(-1px);
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #ffffff !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 12px !important;
            padding: 1.5rem !important;
            margin-bottom: 1rem !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05) !important;
        }

        [data-testid="column"] > [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"]:empty {
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)