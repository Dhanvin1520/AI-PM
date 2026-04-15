import json
import re
import streamlit as st
import os
import logging
from functools import lru_cache
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

# NOTE: Don't initialize the Groq client at import time. On Streamlit Cloud
# the environment variable will be provided via Secrets and importing this
# module before secrets are available can cause the app to crash on startup.
# Initialize the client lazily inside `process_and_rewrite`.

def process_and_rewrite(soup, ad_text):
    """
    Extracts text elements, sends to Groq for rewriting, and updates the soup in-place.
    Implements production-grade error handling and response validation.
    """
    target_tags = ['h1', 'h2', 'h3', 'p', 'a']
    
    elements_to_rewrite = []
    
    for tag_name in target_tags:
        for element in soup.find_all(tag_name):
            text = element.get_text(separator=" ", strip=True)
            if len(text) > 10 and len(text) < 300:
                elements_to_rewrite.append({
                    "tag": tag_name,
                    "original_text": text,
                    "element_ref": element
                })
    
    if not elements_to_rewrite:
        return "No suitable text found to rewrite."
        
    elements_batch = elements_to_rewrite[:30]
    
    prompt_payload = []
    for idx, item in enumerate(elements_batch):
        prompt_payload.append({
            "id": idx,
            "tag": item["tag"],
            "text": item["original_text"]
        })
        
    system_prompt = f"""You are an expert CRO (Conversion Rate Optimization) Specialist and Copywriter for Troopod.
    
Your task is to take the original text from a landing page and rewrite it to perfectly align with the messaging and "vibe" of a specific Ad Creative. 
    
Ad Creative Messaging (Extracted Text from Image): 
"{ad_text}"

You are given a JSON array of text elements from the landing page. 
Instructions:
1. Rewrite 'h1', 'h2', 'h3' to be punchy, benefit-driven, and highly relevant to the Ad Creative.
2. Rewrite 'p' tags to support the new headings and handle user objections.
3. Rewrite 'a' tags (CTAs) to be action-oriented.
4. Output MUST be ONLY a valid JSON array of objects, where each object has 'id' (matching the input) and 'new_text'. Wait, do not wrap in markdown ```json or similar, just pure raw JSON list.
"""

    prompt = f"Original Texts:\n{json.dumps(prompt_payload, indent=2)}\n\nOnly return the JSON list."
    
    try:
        # Ensure API key is available at runtime (Streamlit Cloud uses Secrets)
        groq_key = os.getenv("GROQ_API_KEY")
        if not groq_key:
            st.error("GROQ_API_KEY not found. Add it under Streamlit app Secrets (Settings → Secrets)")
            return False

        client = Groq(api_key=groq_key)

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=6000,
        )
        
        response_text = completion.choices[0].message.content
        
        try:
            clean_json = re.sub(r'```json\n', '', response_text)
            clean_json = re.sub(r'\n```', '', clean_json)
            new_texts = json.loads(clean_json)
            
            for item in new_texts:
                idx = item.get("id")
                new_text = item.get("new_text")
                if idx is not None and new_text:
                    elem_ref = elements_batch[idx]["element_ref"]
                    elem_ref.string = new_text
                    
            return True
        except json.JSONDecodeError:
            st.error("Failed to parse LLM response.")
            st.code(response_text)
            return False
            
    except Exception as e:
        st.error(f"Error during LLM rewriting: {str(e)}")
        return False
