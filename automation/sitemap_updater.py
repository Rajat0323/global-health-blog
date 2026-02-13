import os
from config import POST_FOLDER, DOMAIN

def generate_sitemap():
    # Get project root path
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    public_folder = os.path.join(base_dir, "public")

    os.makedirs(public_folder, exist_ok=True)

    urls = []

    if os.path.exists(POST_FOLDER):
        for file in os.listdir(POST_FOLDER):
            slug = file.replace(".md", "")
            urls.append(f"<url><loc>{DOMAIN}/{slug}</loc></url>")

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{''.join(urls)}
</urlset>
"""

    sitemap_path = os.path.join(public_folder, "sitemap.xml")

    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
