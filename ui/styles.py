import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        .stApp {
            background-color: #ffffff;
        }

        header {display: none;}

        body {
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        }

        h1, h2, h3, p {
            color: #111827;
        }

        .hero-section {
            text-align: center;
            padding: 2.5rem 0;
            border-bottom: 1px solid #e5e7eb;
            margin-bottom: 2rem;
        }

        .title-main {
            font-size: 2.8rem;
            font-weight: 800;
        }

        .subtitle {
            color: #6b7280;
            margin-top: 8px;
        }

        /* FIX UPLOADER */
        [data-testid="stFileUploader"] {
            background: #ffffff !important;
            border: 2px dashed #d1d5db !important;
            border-radius: 12px !important;
            padding: 20px !important;
        }

        /* INPUT */
        .stTextInput input {
            border: 1px solid #d1d5db !important;
            border-radius: 8px !important;
            padding: 10px !important;
        }

        /* BUTTON */
        .stButton button {
            background: linear-gradient(90deg, #4f46e5, #6366f1);
            color: white;
            border-radius: 8px;
            padding: 12px;
            font-weight: 600;
        }

        .stButton button:hover {
            opacity: 0.9;
        }

        /* CARDS */
        [data-testid="stVerticalBlockBorderWrapper"] {
            background: white;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            padding: 20px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.05);
        }
    </style>
    """, unsafe_allow_html=True)