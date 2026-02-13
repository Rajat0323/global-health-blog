import os
from config import LOG_FILE

def is_duplicate(keyword):
    if not os.path.exists(LOG_FILE):
        return False

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return keyword.lower() in f.read().lower()
