import requests
import os

# Get API key from GitHub Secrets
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_article(keyword):

    if not GROQ_API_KEY:
        return f"# {keyword}\n\nGROQ_API_KEY not found."

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    # ✅ FINAL STRUCTURED + SAFE PROMPT
    prompt = f"""
You are a professional medical SEO content writer.

STRICT MARKDOWN RULES (VERY IMPORTANT):
1. Headings must be on their OWN line only.
2. Never write paragraph text on the same line as a heading.
3. Always leave ONE blank line after every heading.
4. Use proper Markdown:
   - # for H1 (only once)
   - ## for H2
   - ### for FAQ questions
   - - for bullet points
5. Do NOT repeat the title inside paragraphs.
6. Do NOT include timestamps or AI mentions.
7. Keep paragraphs short (2–3 lines max).
8. Content must look clean when rendered as HTML.

ARTICLE REQUIREMENTS:
- Word count: 1200–1500 words
- Primary keyword: {keyword}
- Use keyword naturally (6–8 times)
- Include keyword in first 100 words
- Medical accuracy is mandatory

OUTPUT FORMAT (FOLLOW EXACTLY):

---
title: "{keyword}"
date: "2026-02-14"
description: "Learn about {keyword}, including symptoms, causes, treatment options, and when to see a doctor."
---

# {keyword}

Write a 40–50 word direct answer summary optimized for Google Featured Snippet.

## What Is {keyword}?

Write a clear explanation paragraph.

## Causes of {keyword}

- Cause 1
- Cause 2
- Cause 3

## Symptoms of {keyword}

- Symptom 1
- Symptom 2
- Symptom 3

## Risk Factors

Explain briefly in bullet points.

## When to See a Doctor

Explain clearly.

## Diagnosis

Explain briefly.

## Treatment Options

Explain treatment options clearly.

## Prevention Tips

Provide practical prevention tips.

## Frequently Asked Questions

### What is the main cause of {keyword}?
Answer clearly.

### How serious is {keyword}?
Answer clearly.

### Can {keyword} be treated at home?
Answer clearly.

### How long does {keyword} last?
Answer clearly.

### Who is most at risk of {keyword}?
Answer clearly.

## Medical Disclaimer

This article is for informational purposes only and does not substitute professional medical advice.

## References

- World Health Organization (WHO)
- Centers for Disease Control and Prevention (CDC)
- National Institutes of Health (NIH)
- Mayo Clinic
"""

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.6,
        "max_tokens": 2200
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"# {keyword}\n\nAPI Error: {response.text}"

    except Exception as e:
        return f"# {keyword}\n\nRequest Failed: {str(e)}"
