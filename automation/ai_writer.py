import requests
import os

# Get API key from GitHub Secrets
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_article(keyword):

    # If API key missing
    if not GROQ_API_KEY:
        return f"# {keyword}\n\nGROQ_API_KEY not found."

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    # 🔥 ADVANCED SEO PROMPT
    prompt = f"""
You are a professional medical SEO content writer.

Write a 1200–1500 word highly SEO optimized health article.

PRIMARY KEYWORD: {keyword}

STRICT RULES:

1. H1 must be EXACTLY: {keyword}
2. Use the primary keyword naturally at least 7 times.
3. Include the keyword in the first 100 words.
4. Write short paragraphs (2-3 lines max).
5. Use bullet points where helpful.
6. Immediately after H1, write a 40-50 word direct answer summary optimized for Google Featured Snippet.
7. Add medically accurate, trustworthy information.
8. Add a clear "When to See a Doctor" section.
9. Add 5 SEO optimized FAQs (H3 format).
10. Add a Medical Disclaimer section.
11. Add References from trusted sources (WHO, CDC, NIH, Mayo Clinic).
12. Do NOT mention AI.

STRUCTURE FORMAT:

# {keyword}

(40-50 word direct answer summary)

## What Is {keyword}?

## Causes of {keyword}

## Symptoms of {keyword}

## Risk Factors

## When to See a Doctor

## Diagnosis

## Treatment Options

## Prevention Tips

## Frequently Asked Questions

(5 FAQs in ### format)

## Medical Disclaimer

## References
"""

    data = {
        "model": "llama-3.1-8b-instant",  # Updated stable model
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 2000
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"# {keyword}\n\nAPI Error: {response.text}"

    except Exception as e:
        return f"# {keyword}\n\nRequest Failed: {str(e)}"
