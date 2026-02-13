import feedparser

def fetch_health_news():
    urls = [
        "https://news.google.com/rss/search?q=global+health",
        "https://news.google.com/rss/search?q=disease+outbreak",
        "https://news.google.com/rss/search?q=vitamin+deficiency"
    ]

    articles = []
    for url in urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:
            articles.append({
                "title": entry.title,
                "summary": entry.summary
            })

    return articles
