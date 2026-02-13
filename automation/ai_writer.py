import requests
import os

HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
HF_TOKEN = os.getenv("HF_TOKEN")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def generate_article(keyword):
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
            "max_new_tokens": 1500
        }
    }

    response = requests.post(HF_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"# {keyword}\n\nError generating content."
