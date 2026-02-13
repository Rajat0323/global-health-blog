import json

def generate_faq_schema(faqs):
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }

    for q, a in faqs:
        schema["mainEntity"].append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })

    return json.dumps(schema, indent=2)
