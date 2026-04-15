import requests
from bs4 import BeautifulSoup
import streamlit as st
import logging
from typing import Optional


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_landing_page(url: str):
    """Scrapes HTML from the given URL and returns the parsed BeautifulSoup object"""
    if not url or not isinstance(url, str):
        logger.error("Invalid URL provided")
        return None
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        logger.info(f"Successfully scraped {url} - Status: {response.status_code}")
        return BeautifulSoup(response.text, 'html.parser')
    except requests.Timeout:
        error_msg = "Request timeout: Landing page took too long to load"
        logger.error(error_msg)
        st.error(error_msg)
        return None
    except requests.RequestException as e:
        error_msg = f"Failed to fetch landing page: {str(e)}"
        logger.error(error_msg)
        st.error(error_msg)
        return None
