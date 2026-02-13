import os
from config import POST_FOLDER, DOMAIN

def generate_sitemap():
    urls = []

    for file in os.listdir(POST_FOLDER):
        slug = file.replace(".md", "")
        urls.append(f"<url><loc>{DOMAIN}/{slug}</loc></url>")

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{''.join(urls)}
</urlset>
"""

    with open("../public/sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_content)
