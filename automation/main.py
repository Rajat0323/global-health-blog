from keyword_generator import get_random_keyword
from duplicate_checker import is_duplicate
from ai_writer import generate_article
from publisher import save_post, push_to_github
from sitemap_updater import generate_sitemap
from config import LOG_FILE
import csv
from datetime import datetime

def log_keyword(keyword):
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([keyword, datetime.now()])

def main():
    keyword = get_random_keyword()

    if is_duplicate(keyword):
        print("Duplicate keyword. Skipping...")
        return

    print("Generating article for:", keyword)

    content = generate_article(keyword)
    slug = save_post(keyword, content)

    log_keyword(keyword)
    generate_sitemap()
  

    print("Published:", slug)

if __name__ == "__main__":
    main()
