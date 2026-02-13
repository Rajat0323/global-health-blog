import requests
import os

UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_KEY")

def get_image(keyword):
    # If no key, skip image
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

        # If API error, skip image
        if response.status_code != 200:
            print("Unsplash API error:", response.text)
            return None

        data = response.json()

        # SAFE CHECK (no KeyError)
        if isinstance(data, dict) and "results" in data:
            if len(data["results"]) > 0:
                return data["results"][0]["urls"]["regular"]

        return None

    except Exception as e:
        print("Image fetch error:", e)
        return None
