import requests
from bs4 import BeautifulSoup
import streamlit as st
import logging
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_landing_page(url):
    """Scrapes HTML from the given URL and returns the parsed BeautifulSoup object"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        logger.info(f"Successfully scraped {url} - Status: {response.status_code}")
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        st.error(f"Failed to fetch landing page: {str(e)}")
        return None
