import random
from config import KEYWORD_FILE

def load_keywords():
    with open(KEYWORD_FILE, "r", encoding="utf-8") as f:
        return [k.strip() for k in f if k.strip()]

def get_random_keyword():
    keywords = load_keywords()
    return random.choice(keywords)
