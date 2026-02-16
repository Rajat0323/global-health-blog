import requests

INDEXNOW_KEY = "a1b2c3d4e5f6g7h8i9"
SITE_URL = "https://symptomsinsight.com"

def submit_indexnow(urls):
    endpoint = "https://api.indexnow.org/indexnow"
    payload = {
        "host": "symptomsinsight.com",
        "key": INDEXNOW_KEY,
        "keyLocation": f"{SITE_URL}/indexnow.txt",
        "urlList": urls
    }

    r = requests.post(endpoint, json=payload, timeout=10)

    if r.status_code in [200, 202]:
        print("✅ IndexNow submitted successfully")
    else:
        print("❌ IndexNow failed:", r.status_code, r.text)
