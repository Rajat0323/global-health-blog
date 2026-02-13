import subprocess
from config import MODEL_NAME

def generate_article(keyword):
    prompt = f"""
    Write a 1200-word SEO optimized global health article.

    Topic: {keyword}

    Include:
    - H1
    - H2 headings
    - Bullet points
    - 5 FAQs
    - Medical disclaimer
    - References section
    """

    result = subprocess.run(
        ["ollama", "run", MODEL_NAME, prompt],
        capture_output=True,
        text=True
    )

    return result.stdout
