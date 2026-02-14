import requests
import os
import time

HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
HF_TOKEN = os.getenv("HF_TOKEN")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def generate_article(keyword):
    if not HF_TOKEN:
        return f"# {keyword}\n\nHF_TOKEN not found."

    prompt = f"""
Write a 1000-word SEO optimized global health article.

Topic: {keyword}

Include:
- H1 title
- H2 headings
- Bullet points
- 5 FAQs
- Medical disclaimer
- References section
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 1200,
            "temperature": 0.7
        }
    }

    try:
        response = requests.post(
            HF_API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        # If model is loading
        if response.status_code == 503:
            time.sleep(10)
            response = requests.post(
                HF_API_URL,
                headers=headers,
                json=payload,
                timeout=60
            )

        if response.status_code == 200:
            data = response.json()

            # HF sometimes returns list
            if isinstance(data, list) and "generated_text" in data[0]:
                return data[0]["generated_text"]

            # Sometimes returns dict with error
            if isinstance(data, dict) and "error" in data:
                return f"# {keyword}\n\nModel error: {data['error']}"

        return f"# {keyword}\n\nFailed to generate content."

    except Exception as e:
        return f"# {keyword}\n\nException occurred: {str(e)}"
