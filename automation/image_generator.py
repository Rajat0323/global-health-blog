import requests
from config import POST_FOLDER

UNSPLASH_ACCESS_KEY = "YOUR_UNSPLASH_KEY"

def get_image(keyword):
    url = f"https://api.unsplash.com/search/photos"
    params = {
        "query": keyword,
        "client_id": UNSPLASH_ACCESS_KEY,
        "per_page": 1
    }

    res = requests.get(url, params=params).json()

    if res["results"]:
        return res["results"][0]["urls"]["regular"]

    return None
