from services.news_service import NewsService


class ResearchService:

    def __init__(self):

        self.news_service = NewsService()

    def get_research(self, topic):

        articles = self.news_service.get_news(topic)

        research = ""

        for i, article in enumerate(articles, start=1):

            research += f"""
News {i}

Title:
{article["title"]}

Summary:
{article["summary"]}

"""

        return research