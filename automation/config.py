import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

KEYWORD_FILE = os.path.join(BASE_DIR, "data", "keywords.txt")
TOPIC_FILE = os.path.join(BASE_DIR, "data", "health_topics.json")
LOG_FILE = os.path.join(BASE_DIR, "logs", "processed_articles.csv")
ERROR_LOG = os.path.join(BASE_DIR, "logs", "error_log.txt")
POST_FOLDER = os.path.join(BASE_DIR, "posts", "2026")

DOMAIN = "https://symptomsinsight.com"
MODEL_NAME = "mistral"
