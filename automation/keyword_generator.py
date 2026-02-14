import random
from config import KEYWORD_FILE

def get_random_keyword():
    try:
        with open(KEYWORD_FILE, "r", encoding="utf-8") as f:
            keywords = [line.strip() for line in f if line.strip()]

        if not keywords:
            print("No keywords found.")
            return None

        return random.choice(keywords)

    except Exception as e:
        print("Keyword loading error:", e)
        return None
