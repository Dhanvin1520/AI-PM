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
        uploaded_file = st.file_uploader("Upload Image (JPG/PNG)", type=['jpg', 'jpeg', 'png'], label_visibility="collapsed")
        if uploaded_file is not None:
            st.image(uploaded_file, caption="Uploaded Ad Target", use_container_width=True)

    with st.container(border=True):
        st.markdown("### 2. Target Landing Page")
        st.caption("The exact URL that the ad currently points to.")
        target_url = st.text_input("Landing Page URL (e.g. https://example.com)", label_visibility="collapsed", placeholder="https://example.com")

    with st.expander("⚙️ How this Agentic Engine works"):
        st.markdown("""
        1. **Ad Parsing**: Uses high-speed OCR to read the exact copy and offer off the image.
        2. **DOM Extraction**: Headless parser strips your landing page down to variable text nodes.
        3. **LLaMA Synthesis**: Groq's 70B Model rewrites the target nodes explicitly matching the logic & CRO conversion principles to the Ad's vibe.
        4. **Live Re-Rendering**: We immediately inject the optimized variant directly back into the live HTML.
        """)


    generate_pressed = st.button("Generate Personalized Layout", type="primary", use_container_width=True)
    
    if generate_pressed:
        if uploaded_file is None or not target_url:
            st.error("⚠️ Please upload an ad creative and provide a landing page URL.")
        else:
            with st.spinner("🔄 Processing..."):
                progress_placeholder = st.empty()
                try:
                    progress_placeholder.info("📸 Extracting ad text...")
                    ad_text = extract_text_from_image(uploaded_file)
                    
                    progress_placeholder.info("🌐 Fetching landing page...")
                    page_html = scrape_landing_page(target_url)
                    
                    progress_placeholder.info("🤖 Optimizing with AI...")
                    result = process_and_rewrite(page_html, ad_text)
                    
                    progress_placeholder.success("✅ Done!")
                    time.sleep(1)
                    progress_placeholder.empty()
                except Exception as e:
                    progress_placeholder.error(f"Error: {str(e)}")

if generate_pressed:
    if not uploaded_file:
        st.warning("Upload an ad creative first.")
    elif not target_url:
        st.warning("Enter a landing page URL.")
    else:
        image_bytes = uploaded_file.getvalue()
        extracted_ad_text = extract_text_from_image(image_bytes)
        soup = scrape_landing_page(target_url)
        
        if soup:
            original_html = str(soup)
            
            for a in soup.find_all('a'):
                a['target'] = '_blank'
            
            success = process_and_rewrite(soup, extracted_ad_text)
            
            if success:
                st.markdown("<br>", unsafe_allow_html=True)
                

                st.markdown("## 📊 Your Optimized Landing Page")
                
                final_html = str(soup)
                parsed_url = target_url.split('/')
                base_url = f"{parsed_url[0]}//{parsed_url[2]}"
                final_html = final_html.replace("<head>", f"<head><base href='{base_url}/'>")
                
       
                col_preview, col_download = st.columns([4, 1])
                
                with col_download:
                    st.markdown("<br>", unsafe_allow_html=True)
                    b64 = base64.b64encode(final_html.encode('utf-8')).decode()
                    st.markdown(f'<a href="data:text/html;base64,{b64}" download="optimized.html" style="display:block; background-color: #4f46e5; color: white; padding: 12px; text-align: center; border-radius: 8px; text-decoration: none; font-weight: 600; cursor: pointer;">⬇️ Download</a>', unsafe_allow_html=True)
                
                with col_preview:
                    st.components.v1.html(final_html, height=600, scrolling=True)
