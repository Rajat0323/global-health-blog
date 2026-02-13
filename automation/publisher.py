import os
from datetime import datetime
from config import POST_FOLDER, DOMAIN
from image_generator import get_image   # ✅ import correct

# -----------------------------
# Find Related Posts
# -----------------------------
def find_related_posts(keyword):
    related = []

    for file in os.listdir(POST_FOLDER):
        if keyword.split()[0].lower() in file.lower():
            slug = file.replace(".md", "")
            related.append(
                f"- [{slug.replace('-', ' ').title()}]({DOMAIN}/{slug})"
            )

    return related[:3]


# -----------------------------
# Save Markdown File
# -----------------------------
def save_post(keyword, content):

    slug = keyword.lower().replace(" ", "-")
    filepath = os.path.join(POST_FOLDER, f"{slug}.md")

    # ✅ Get Featured Image
    image_url = get_image(keyword)

    # ✅ Find related posts
    related_links = find_related_posts(keyword)

    with open(filepath, "w", encoding="utf-8") as f:

        # -----------------------------
        # Frontmatter
        # -----------------------------
        f.write("---\n")
        f.write(f"title: \"{keyword.title()}\"\n")
        f.write(f"date: \"{datetime.now()}\"\n")
        f.write(f"slug: \"{slug}\"\n")

        if image_url:
            f.write(f"image: \"{image_url}\"\n")

        f.write("---\n\n")

        # -----------------------------
        # Article Content
        # -----------------------------
        f.write(content)

        # -----------------------------
        # Related Articles Section
        # -----------------------------
        if related_links:
            f.write("\n\n## Related Articles\n\n")
            for link in related_links:
                f.write(link + "\n")

    return slug


# -----------------------------
# Push to GitHub
# -----------------------------
def push_to_github():
    os.system("git add .")
    os.system("git commit -m 'New health article added'")
    os.system("git push origin main")
