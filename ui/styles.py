import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        .stApp {
            background-color: #ffffff !important;
        }

        body {
            font-family: 'Inter', sans-serif;
        }

        header {display: none !important;}

        h1, h2, h3, p, span, div, label {
            color: #0f172a !important;
        }

        .hero-section {
            padding: 3rem 0 2rem 0;
            margin-bottom: 2rem;
            border-bottom: 1px solid #e5e7eb;
            text-align: center;
        }

        .title-main {
            font-size: 3rem;
            font-weight: 800;
            letter-spacing: -0.04em;
        }

        .subtitle {
            color: #64748b;
            font-size: 1.1rem;
            margin-top: 0.5rem;
        }

        .stTextInput > div > div > input {
            background-color: #ffffff !important;
            color: #0f172a !important;
            border: 1px solid #d1d5db !important;
            border-radius: 8px;
            padding: 0.75rem;
        }

        .stButton > button {
            background-color: #4f46e5 !important;
            color: white !important;
            border-radius: 8px !important;
            padding: 0.75rem !important;
            font-weight: 600 !important;
            width: 100%;
        }

        .stButton > button:hover {
            background-color: #4338ca !important;
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #ffffff !important;
            border: 1px solid #e5e7eb !important;
            border-radius: 12px !important;
            padding: 1.5rem !important;
            margin-bottom: 1rem !important;
            box-shadow: 0 10px 25px rgba(0,0,0,0.06) !important;
        }
    </style>
    """, unsafe_allow_html=True)