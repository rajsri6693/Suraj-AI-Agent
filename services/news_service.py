import re
from html import unescape
from urllib.parse import quote

import feedparser


class NewsService:

    def clean_html(self, text):

        text = re.sub(r"<.*?>", "", text)

        text = unescape(text)

        return text.strip()

    def get_news(self, topic):

        encoded_topic = quote(topic)

        url = f"https://news.google.com/rss/search?q={encoded_topic}"

        feed = feedparser.parse(url)

        news = []

        for item in feed.entries[:5]:

            news.append({
                "title": self.clean_html(item.title),
                "summary": self.clean_html(item.summary)
            })

        return news