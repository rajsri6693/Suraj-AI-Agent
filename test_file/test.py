from services.news_service import NewsService

news = NewsService()

articles = news.get_news("Nifty 50")

for article in articles:

    print(article["title"])
    print(article["summary"])
    print("-" * 60)