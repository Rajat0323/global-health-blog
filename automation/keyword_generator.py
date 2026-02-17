import os
import csv
from config import KEYWORD_FILE, LOG_FILE


def get_processed_keywords():
    processed = set()

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    processed.add(row[0].strip().lower())

    return processed



BASE_DIR = os.path.dirname(os.path.dirname(__file__))
KEYWORDS_FILE = os.path.join(BASE_DIR, "keywords.txt")

def get_next_keyword():
    with open(KEYWORDS_FILE, "r", encoding="utf-8") as f:
        keywords = [k.strip() for k in f if k.strip()]

    if not keywords:
        return None

    next_keyword = keywords[0]

    # 🔥 REMOVE USED KEYWORD
    with open(KEYWORDS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(keywords[1:]))

    return next_keyword

