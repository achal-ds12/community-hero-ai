import os
import json
from dotenv import load_dotenv
from google import genai
from PIL import Image

# Load API key
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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

    response = client.models.generate_content(
        model=MODEL,
        contents=[
            prompt,
            image
        ]
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)