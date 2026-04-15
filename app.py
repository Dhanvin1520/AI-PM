import streamlit as st
import base64

from ui.styles import apply_custom_styles
from backend.ocr_engine import extract_text_from_image
from backend.scraper import scrape_landing_page
from backend.llm_engine import process_and_rewrite

st.set_page_config(
    page_title="AI Landing Page Personalizer",
    layout="centered"
)

apply_custom_styles()

# HERO
st.markdown("""
<div class="hero-section">
    <div class="hero-badge">AI-Powered CRO Tool</div>
    <h1 class="title-main">Landing Page Personalizer Engine</h1>
    <p class="subtitle">Align your landing page content with ad creatives using AI-driven personalization.</p>
</div>
""", unsafe_allow_html=True)

# UPLOAD
st.markdown("### 1. Upload Ad Creative")
uploaded_file = st.file_uploader("", type=["jpg","png","jpeg"])

if uploaded_file:
    st.image(uploaded_file, use_container_width=True)

# URL INPUT
st.markdown("### 2. Target Landing Page")
target_url = st.text_input("", placeholder="https://example.com")

# HOW IT WORKS
with st.expander("How this Agent works"):
    st.markdown("""
    1. Extracts text from ad  
    2. Scrapes landing page  
    3. AI rewrites content  
    4. Shows optimized version  
    """)

# BUTTON
generate = st.button("Generate Personalized Layout", use_container_width=True)

# PROCESS
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

                for a in soup_modified.find_all("a"):
                    a["target"] = "_blank"

                process_and_rewrite(soup_modified, ad_text)

                original_html = str(soup_original)
                modified_html = str(soup_modified)

                parsed = target_url.split("/")
                base = f"{parsed[0]}//{parsed[2]}"

                original_html = original_html.replace("<head>", f"<head><base href='{base}/'>")
                modified_html = modified_html.replace("<head>", f"<head><base href='{base}/'>")

                st.markdown("## Comparison")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("### Original")
                    st.components.v1.html(original_html, height=600)

                with col2:
                    st.markdown("### Personalized")
                    st.components.v1.html(modified_html, height=600)

                b64 = base64.b64encode(modified_html.encode()).decode()

                st.markdown(
                    f'<a href="data:text/html;base64,{b64}" download="optimized.html" '
                    f'style="display:block;background:#0284c7;color:white;padding:10px;text-align:center;border-radius:8px;text-decoration:none;">Download</a>',
                    unsafe_allow_html=True
                )

            except Exception as e:
                st.error(str(e))