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


def get_next_keyword():
    if not os.path.exists(KEYWORD_FILE):
        print("Keyword file not found.")
        return None

    processed = get_processed_keywords()

    with open(KEYWORD_FILE, "r", encoding="utf-8") as f:
        for line in f:
            keyword = line.strip()
            if keyword and keyword.lower() not in processed:
                return keyword

    return None
