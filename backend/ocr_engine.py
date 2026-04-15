import requests
import json
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
    except requests.Timeout:
        logger.error("OCR API request timeout")
        return "Error: OCR service timeout. Please try again."
    except requests.RequestException as e:
        logger.error(f"OCR API request failed: {str(e)}")
        return "Error: Failed to connect to OCR service."
    except json.JSONDecodeError:
        logger.error("Invalid JSON response from OCR API")
        return "Error: Invalid response from OCR service."
    except Exception as e:
        logger.error(f"Unexpected error in OCR: {str(e)}")
        return f"Error: {str(e)}"
