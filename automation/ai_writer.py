import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_article(keyword):
    if not GROQ_API_KEY:
        return f"# {keyword}\n\nGROQ_API_KEY not found."

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {
                "role": "user",
                "content": f"""
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
            }
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]

        return f"# {keyword}\n\nAPI Error: {response.text}"

    except Exception as e:
        return f"# {keyword}\n\nException: {str(e)}"
