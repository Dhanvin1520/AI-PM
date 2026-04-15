import requests
import logging
from functools import lru_cache
from typing import Optional


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_text_from_image(image_bytes):
    """Uses OCR.space free API to extract text from an image"""
    try:
        url = 'https://api.ocr.space/parse/image'
        

        payload = {
            'apikey': 'helloworld',
            'isOverlayRequired': False,
            'language': 'eng'
        }
        
        files = {
            'image': ('image.jpg', image_bytes, 'image/jpeg')
        }
        
        response = requests.post(url, data=payload, files=files)
        result = response.json()
        
        logger.info(f"OCR API Response - Status: {result.get('IsErroredOnProcessing')}")
        
        if result.get('ParsedResults') and len(result['ParsedResults']) > 0:
            extracted = result['ParsedResults'][0]['ParsedText']
            if extracted:
                logger.info(f"Successfully extracted {len(extracted)} characters")
                return extracted.strip()
        logger.warning("No text detected in image")
        return "No text detected."
    except Exception as e:
        return f"Error extracting text: {str(e)}"
