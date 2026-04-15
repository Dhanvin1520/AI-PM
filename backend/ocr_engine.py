import requests

def extract_text_from_image(image_bytes):
    """Uses OCR.space free API to extract text from an image"""
    try:
        url = 'https://api.ocr.space/parse/image'
        
        # Free API key specifically for general public use
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
        
        if result.get('ParsedResults') and len(result['ParsedResults']) > 0:
            extracted = result['ParsedResults'][0]['ParsedText']
            return extracted.strip()
        return "No text detected."
    except Exception as e:
        return f"Error extracting text: {str(e)}"
