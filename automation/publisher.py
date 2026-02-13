import os
from datetime import datetime
from config import POST_FOLDER, DOMAIN
from image_generator import get_image


def find_related_posts(keyword):
    related = []
    main_word = keyword.split()[0].lower()

    for file in os.listdir(POST_FOLDER):
        if main_word in file.lower():
            slug = file.replace(".md", "")
            related.append(
                f"- [{slug.replace('-', ' ').title()}]({DOMAIN}/{slug})"
            )

    return related[:3]


def save_post(keyword, content):
    os.makedirs(POST_FOLDER, exist_ok=True)  # ADD THIS
    slug = keyword.lower().replace(" ", "-")
    filepath = os.path.join(POST_FOLDER, f"{slug}.md")

    related_links = find_related_posts(keyword)
    image_url = get_image(keyword) or ""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"title: \"{keyword.title()}\"\n")
        f.write(f"date: \"{datetime.now().isoformat()}\"\n")
        f.write(f"slug: \"{slug}\"\n")

        if image_url:
            f.write(f"image: \"{image_url}\"\n")

        f.write("---\n\n")
        f.write(content)

        if related_links:
            f.write("\n\n## Related Articles\n\n")
            for link in related_links:
                f.write(link + "\n")

    return slug
