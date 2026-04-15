import requests
from bs4 import BeautifulSoup
import json
import os
import logging
from dotenv import load_dotenv
from groq import Groq

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

def test_ocr():
    logger.info("Testing OCR Engine...")
    try:
        image_bytes = b"dummy image content just to test endpoint connection"
        url = 'https://api.ocr.space/parse/image'
        payload = {'apikey': 'helloworld', 'isOverlayRequired': False, 'language': 'eng'}
        files = {'image': ('test.jpg', image_bytes, 'image/jpeg')}
        res = requests.post(url, data=payload, files=files, timeout=10)
        res.raise_for_status()
        logger.info(f"✓ OCR Status: {res.status_code}")
    except requests.Timeout:
        logger.error("✗ OCR API timeout")
    except requests.RequestException as e:
        logger.error(f"✗ OCR Error: {str(e)}")

def test_groq():
    logger.info("Testing Groq API...")
    try:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            logger.error("✗ GROQ_API_KEY not set in environment")
            return
        client = Groq(api_key=api_key)
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": "Say hello"}],
            max_tokens=10
        )
        logger.info(f"✓ Groq Response: {completion.choices[0].message.content}")
    except Exception as e:
        logger.error(f"✗ Groq Error: {str(e)}")

def test_imports():
    logger.info("Testing Module Imports...")
    try:
        from backend.ocr_engine import extract_text_from_image
        from backend.scraper import scrape_landing_page
        from backend.llm_engine import process_and_rewrite
        from ui.styles import apply_custom_styles
        logger.info("✓ All modules imported successfully")
        return True
    except ImportError as e:
        logger.error(f"✗ Import Error: {str(e)}")
        return False

if __name__ == "__main__":
    logger.info("Starting test suite...\n")
    test_imports()
    logger.info("")
    test_ocr()
    logger.info("")
    test_groq()
    logger.info("\nTest suite completed.")
