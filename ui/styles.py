import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        .stApp {
            background: #ffffff !important;
        }

        /* REMOVE WHITE OVERLAY */
        .block-container {
            background: transparent !important;
            padding-top: 2rem !important;
        }

        section[data-testid="stAppViewContainer"] {
            background: transparent !important;
        }

        /* REMOVE TOP BLACK BAR */
        header {visibility: hidden;}

        /* TEXT */
        body, h1, h2, h3, p {
            color: #111827 !important;
            font-family: -apple-system, sans-serif;
        }

        /* CENTER CONTAINER */
        .main .block-container {
            max-width: 900px;
            margin: auto;
        }

        /* FILE UPLOADER FIX */
        [data-testid="stFileUploader"] {
            background: #ffffff !important;
            border: 2px dashed #d1d5db !important;
            border-radius: 12px !important;
            padding: 20px !important;
        }

        /* BUTTON */
        .stButton button {
            background: linear-gradient(90deg, #4f46e5, #6366f1);
            color: white;
            border-radius: 8px;
            padding: 12px;
            font-weight: 600;
            width: 100%;
        }

        /* INPUT */
        .stTextInput input {
            border-radius: 8px !important;
            border: 1px solid #d1d5db !important;
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