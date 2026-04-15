import streamlit as st
import base64

from ui.styles import apply_custom_styles
from backend.ocr_engine import extract_text_from_image
from backend.scraper import scrape_landing_page
from backend.llm_engine import process_and_rewrite

st.set_page_config(page_title="Troopod AI PM Assignment", page_icon="✨", layout="wide")

apply_custom_styles()

st.markdown("""
<div class="hero-section">
    <h1 class="title-main">Landing Page Personalizer Engine</h1>
    <p class="subtitle">Data-driven landing page optimization aligned with your ad creatives.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 1. Upload Ad Creative")
uploaded_file = st.file_uploader("", type=['jpg','jpeg','png'])

st.markdown("### 2. Target Landing Page")
target_url = st.text_input("", placeholder="https://example.com")

generate = st.button("Generate Personalized Layout")

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

                    st.markdown("## Comparison View")

                    original_html = str(soup_original)
                    modified_html = str(soup_modified)

                    parsed = target_url.split('/')
                    base = f"{parsed[0]}//{parsed[2]}"

                    original_html = original_html.replace("<head>", f"<head><base href='{base}/'>")
                    modified_html = modified_html.replace("<head>", f"<head><base href='{base}/'>")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown("###  Original Page")
                        st.components.v1.html(original_html, height=600, scrolling=True)

                    with col2:
                        st.markdown("###  Personalized Page")
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