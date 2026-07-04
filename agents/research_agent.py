from services.research_service import ResearchService
from services.gemini_service import GeminiService


class ResearchAgent:

    def __init__(self):

        self.research_service = ResearchService()
        self.gemini = GeminiService()

    def generate(self, topic):

        print("\nResearching Latest News...\n")

        latest_news = self.research_service.get_research(topic)

        print("Generating Research Summary...\n")

        summary = self.gemini.generate_research(
            topic,
            latest_news
        )

        return summary