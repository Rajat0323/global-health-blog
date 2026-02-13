import os
from sentence_transformers import SentenceTransformer, util
from config import POST_FOLDER, DOMAIN

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_related_posts(new_content):
    files = os.listdir(POST_FOLDER)

    related = []
    new_embedding = model.encode(new_content, convert_to_tensor=True)

    for file in files:
        with open(os.path.join(POST_FOLDER, file), "r", encoding="utf-8") as f:
            content = f.read()

        old_embedding = model.encode(content, convert_to_tensor=True)
        score = util.cos_sim(new_embedding, old_embedding)

        if score > 0.5:
            slug = file.replace(".md", "")
            related.append((slug, score.item()))

    related.sort(key=lambda x: x[1], reverse=True)

    links = [
        f"- [{slug.replace('-', ' ').title()}]({DOMAIN}/{slug})"
        for slug, _ in related[:3]
    ]

    return links
