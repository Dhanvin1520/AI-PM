import requests
from bs4 import BeautifulSoup
import json
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def test_ocr():
    print("Testing OCR...")
    # create dummy image
    image_bytes = b"dummy image content just to test endpoint connection"
    url = 'https://api.ocr.space/parse/image'
    payload = {'apikey': 'helloworld', 'isOverlayRequired': False, 'language': 'eng'}
    files = {'image': ('test.jpg', image_bytes, 'image/jpeg')}
    try:
        res = requests.post(url, data=payload, files=files)
        print("OCR Status:", res.status_code)
        print("OCR Response:", res.text[:200])
    except Exception as e:
        print("OCR Error:", str(e))

def test_groq():
    print("Testing Groq...")
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": "Say hello"}],
            max_tokens=10
        )
        print("Groq Response:", completion.choices[0].message.content)
    except Exception as e:
        print("Groq Error:", str(e))

if __name__ == "__main__":
    test_ocr()
    test_groq()
