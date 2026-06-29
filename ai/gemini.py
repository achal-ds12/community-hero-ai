import json
import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from PIL import Image

# Load .env for local development
load_dotenv()

# Get API key (Streamlit Cloud -> Secrets, Local -> .env)
api_key = None

try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found.")

client = genai.Client(api_key=api_key)

MODEL = "gemini-2.5-flash"


def analyze_issue(description, image_path):
    image = Image.open(image_path)

    prompt = f"""
You are an AI assistant for a smart civic issue reporting platform.

Analyze BOTH:
1. The uploaded image.
2. The user's description.

Description:
{description}

Return ONLY valid JSON.

{{
    "category": "",
    "severity": "",
    "priority": "",
    "department": "",
    "summary": "",
    "recommended_action": ""
}}
"""

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=[prompt, image]
        )

        text = response.text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "").replace("```", "").strip()

        return json.loads(text)

    except Exception as e:
        return {
            "category": "Unknown",
            "severity": "Medium",
            "priority": "Normal",
            "department": "Municipal Department",
            "summary": f"AI service temporarily unavailable: {str(e)}",
            "recommended_action": "Please review the issue manually."
        }