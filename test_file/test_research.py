from services.research_service import ResearchService

research = ResearchService()

result = research.get_research("Nifty 50")

print(result)