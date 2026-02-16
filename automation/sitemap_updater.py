import os
from datetime import datetime

SITE_URL = "https://symptomsinsight.com"
POSTS_DIR = "posts"
SITEMAP_PATH = "public/sitemap.xml"

def generate_sitemap():
    urls = []

    for year in os.listdir(POSTS_DIR):
        year_path = os.path.join(POSTS_DIR, year)
        if not os.path.isdir(year_path):
            continue

        for file in os.listdir(year_path):
            if file.endswith(".md"):
                slug = file.replace(".md", "")
                urls.append(f"{SITE_URL}/blog/{slug}")

    with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

        f.write(f"""
  <url>
    <loc>{SITE_URL}/</loc>
    <lastmod>{datetime.now().date()}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
""")

        for url in urls:
            f.write(f"""
  <url>
    <loc>{url}</loc>
    <lastmod>{datetime.now().date()}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
""")

        f.write('</urlset>')

    print("✅ Sitemap updated:", SITEMAP_PATH)
