from keyword_generator import get_next_keyword
from duplicate_checker import is_duplicate
from ai_writer import generate_article
from publisher import save_post
from config import LOG_FILE
from indexnow import submit_indexnow

import csv
from datetime import datetime


def log_keyword(keyword):
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([keyword, datetime.now()])


def main():
    print("Automation started")

    # Get next unused keyword
    keyword = get_next_keyword()
    print("Keyword:", keyword)

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

    # Save markdown file → slug CREATED HERE
    slug = save_post(keyword, content)
    print("Slug created:", slug)

    # Log keyword
    log_keyword(keyword)

    # ✅ IndexNow submit (MUST be inside main)
    new_url = f"https://symptomsinsight.com/blog/{slug}"
    submit_indexnow([new_url])

    print("Published & IndexNow pinged:", new_url)


if __name__ == "__main__":
    main()
