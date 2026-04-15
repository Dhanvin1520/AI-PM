import streamlit as st
import time
import base64

from ui.styles import apply_custom_styles
from backend.ocr_engine import extract_text_from_image
from backend.scraper import scrape_landing_page
from backend.llm_engine import process_and_rewrite

st.set_page_config(page_title="Troopod AI PM Assignment", page_icon="✨", layout="wide")

apply_custom_styles()

st.markdown('''
<div class="hero-section">
    <h1 class="title-main">Landing Page Personalizer Engine</h1>
    <p class="subtitle">Data-driven landing page optimization aligned with your ad creatives.</p>
</div>
''', unsafe_allow_html=True)

_, center_col, _ = st.columns([1, 3, 1])

with center_col:
    with st.container(border=True):
        st.markdown("### 1. Upload Ad Creative")
        st.caption("Upload the display ad or creative asset from your campaign.")
        uploaded_file = st.file_uploader("", type=['jpg', 'jpeg', 'png'])
        if uploaded_file:
            st.image(uploaded_file, use_container_width=True)

    with st.container(border=True):
        st.markdown("### 2. Target Landing Page")
        st.caption("The exact URL that the ad currently points to.")
        target_url = st.text_input("", placeholder="https://example.com")

    with st.expander("⚙️ How this Agentic Engine works"):
        st.markdown("""
        1. Ad Parsing using OCR  
        2. Landing Page DOM extraction  
        3. LLM rewrite using Groq  
        4. Live HTML injection  
        """)

    generate = st.button("Generate Personalized Layout", type="primary", use_container_width=True)

if generate:
    if not uploaded_file or not target_url:
        st.error("Upload image and enter URL")
    else:
        with st.spinner("Processing..."):
            try:
                image_bytes = uploaded_file.getvalue()
                ad_text = extract_text_from_image(image_bytes)

                soup_original = scrape_landing_page(target_url)
                soup_modified = scrape_landing_page(target_url)

                if soup_original and soup_modified:

                    for a in soup_modified.find_all('a'):
                        a['target'] = '_blank'

                    process_and_rewrite(soup_modified, ad_text)

                    st.markdown("## 📊 Comparison View")

                    original_html = str(soup_original)
                    modified_html = str(soup_modified)

                    parsed_url = target_url.split('/')
                    base_url = f"{parsed_url[0]}//{parsed_url[2]}"

                    original_html = original_html.replace("<head>", f"<head><base href='{base_url}/'>")
                    modified_html = modified_html.replace("<head>", f"<head><base href='{base_url}/'>")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown("### 🌐 Original Page")
                        st.components.v1.html(original_html, height=600, scrolling=True)

                    with col2:
                        st.markdown("### 🚀 Personalized Page")
                        st.components.v1.html(modified_html, height=600, scrolling=True)

                    st.markdown("### ⬇️ Download Personalized Page")

                    b64 = base64.b64encode(modified_html.encode()).decode()
                    st.markdown(
                        f'<a href="data:text/html;base64,{b64}" download="optimized.html" '
                        f'style="display:block;background:#4f46e5;color:white;padding:12px;text-align:center;border-radius:8px;text-decoration:none;font-weight:600;">Download</a>',
                        unsafe_allow_html=True
                    )

            except Exception as e:
                st.error(str(e))