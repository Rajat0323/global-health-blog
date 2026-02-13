import requests
import os

UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_KEY")

def get_image(keyword):
    if not UNSPLASH_ACCESS_KEY:
        return None

    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": keyword,
        "client_id": UNSPLASH_ACCESS_KEY,
        "per_page": 1
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()

        if "results" in data and len(data["results"]) > 0:
            return data["results"][0]["urls"]["regular"]

        return None

    except Exception:
        return None
