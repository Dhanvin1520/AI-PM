import streamlit as st
import base64

from ui.styles import apply_custom_styles
from backend.ocr_engine import extract_text_from_image
from backend.scraper import scrape_landing_page
from backend.llm_engine import process_and_rewrite

st.set_page_config(
    page_title="Troopod AI PM",
    page_icon="🚀",
    layout="wide"
)

apply_custom_styles()

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-section">
    <h1 class="title-main">🚀 Landing Page Personalizer Engine</h1>
    <p class="subtitle">Data-driven landing page optimization aligned with your ad creatives.</p>
</div>
""", unsafe_allow_html=True)

# ── Inputs ────────────────────────────────────────────────────────────────────
col_left, col_right = st.columns(2, gap="large")

with col_left:
    st.markdown('<p class="section-label">1 · Upload Ad Creative</p>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        label="upload",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Creative", use_container_width=True)

with col_right:
    st.markdown('<p class="section-label">2 · Target Landing Page URL</p>', unsafe_allow_html=True)
    target_url = st.text_input(
        label="url",
        placeholder="https://example.com",
        label_visibility="collapsed"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("⚙️ How this Agent works"):
        st.markdown("""
        1. **Extracts** text & intent from your ad creative  
        2. **Scrapes** the target landing page  
        3. **Rewrites** page content with AI to match ad messaging  
        4. **Shows** side-by-side original vs personalised view  
        """)

    st.markdown("<br>", unsafe_allow_html=True)
    generate = st.button("⚡ Generate Personalized Layout", use_container_width=True)

# ── Processing ────────────────────────────────────────────────────────────────
if generate:
    if not uploaded_file or not target_url:
        st.error("⚠️ Please upload an ad creative AND enter a target URL before generating.")
    else:
        with st.spinner("🔍 Analysing creative & rewriting page…"):
            try:
                image_bytes = uploaded_file.getvalue()
                ad_text = extract_text_from_image(image_bytes)

                soup_original = scrape_landing_page(target_url)
                soup_modified = scrape_landing_page(target_url)

                if soup_original and soup_modified:
                    for a in soup_modified.find_all("a"):
                        a["target"] = "_blank"

                    process_and_rewrite(soup_modified, ad_text)

                    parsed = target_url.split("/")
                    base = f"{parsed[0]}//{parsed[2]}"

                    original_html = str(soup_original).replace(
                        "<head>", f"<head><base href='{base}/'>"
                    )
                    modified_html = str(soup_modified).replace(
                        "<head>", f"<head><base href='{base}/'>"
                    )

                    # ── Download (shown first, above comparison) ──────────────
                    st.markdown("---")
                    b64 = base64.b64encode(modified_html.encode()).decode()
                    st.markdown(
                        f'<a href="data:text/html;base64,{b64}" download="optimized.html" '
                        f'class="download-btn">⬇ Download Personalised Page</a>',
                        unsafe_allow_html=True,
                    )
                    st.markdown("<br>", unsafe_allow_html=True)

                    # ── Side-by-side comparison ───────────────────────────────
                    st.markdown('<p class="section-label">📊 Comparison View</p>', unsafe_allow_html=True)

                    c1, c2 = st.columns(2, gap="medium")
                    with c1:
                        st.markdown("**Original Page**")
                        st.components.v1.html(original_html, height=620, scrolling=True)
                    with c2:
                        st.markdown("**Personalised Page**")
                        st.components.v1.html(modified_html, height=620, scrolling=True)

            except Exception as e:
                st.error(f"Something went wrong: {e}")