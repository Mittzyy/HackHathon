# src/translator.py

import requests, logging
from .config import AZURE_TRANSLATOR_KEY, AZURE_TRANSLATOR_ENDPOINT, REGION

def translate(text: str, to: str = "id") -> str:
    url = (
        f"{AZURE_TRANSLATOR_ENDPOINT}/translator/text/v3.0/translate"
        f"?api-version=3.0&to={to}"
    )
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_TRANSLATOR_KEY,
        "Ocp-Apim-Subscription-Region": REGION,
        "Content-Type": "application/json"
    }
    body = [{"text": text}]
    try:
        resp = requests.post(url, headers=headers, json=body, timeout=5)
        resp.raise_for_status()
        return resp.json()[0]["translations"][0]["text"]
    except Exception as e:
        logging.getLogger("uvicorn.error").warning("Translate(%s) error: %s", to, e)
        return text

def translate_to_id(text: str) -> str:
    return translate(text, to="id")

def translate_to_en(text: str) -> str:
    return translate(text, to="en")

def detect_language(text: str) -> str:
    """
    Use Azure Translator detect endpoint to return language code
    """
    url = f"{AZURE_TRANSLATOR_ENDPOINT}/translator/text/v3.0/detect?api-version=3.0"
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_TRANSLATOR_KEY,
        "Ocp-Apim-Subscription-Region": REGION,
        "Content-Type": "application/json"
    }
    body = [{"text": text}]
    try:
        resp = requests.post(url, headers=headers, json=body, timeout=5)
        resp.raise_for_status()
        langs = resp.json()[0]["language"]
        return langs
    except Exception as e:
        logging.getLogger("uvicorn.error").warning("Detect language error: %s", e)
        # fallback: basic heuristic English keywords
        first = text.strip().split()[0].lower()
        return "en" if first in ("what","how","who","when","where","why") else "id"
