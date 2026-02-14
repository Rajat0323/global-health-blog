import os
import csv
from config import KEYWORD_FILE, LOG_FILE

def get_next_keyword():
    # Load all keywords
    with open(KEYWORD_FILE, "r", encoding="utf-8") as f:
        keywords = [k.strip() for k in f.readlines() if k.strip()]

    processed = []

    # Load processed keywords if file exists
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    processed.append(row[0].strip())

    # Find first unused keyword
    for keyword in keywords:
        if keyword not in processed:
            return keyword

    return None
