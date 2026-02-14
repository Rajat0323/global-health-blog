from keyword_generator import get_next_keyword
from duplicate_checker import is_duplicate
from ai_writer import generate_article
from publisher import save_post
from sitemap_updater import generate_sitemap
from config import LOG_FILE
import csv
from datetime import datetime


def log_keyword(keyword):
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([keyword, datetime.now()])


def main():
    # Get next unused keyword
    keyword = get_next_keyword()

    if not keyword:
        print("No new keywords available.")
        return

    # Check duplicate safety
    if is_duplicate(keyword):
        print("Duplicate keyword. Skipping...")
        return

    print("Generating article for:", keyword)

    # Generate AI content
    content = generate_article(keyword)

    # Save markdown file
    slug = save_post(keyword, content)

    # Log keyword
    log_keyword(keyword)

    # Regenerate sitemap
    generate_sitemap()

    print("Published:", slug)


if __name__ == "__main__":
    main()
