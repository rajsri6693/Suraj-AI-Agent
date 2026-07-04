from agents.research_agent import ResearchAgent
from agents.content_agent import ContentAgent

from services.notion_service import NotionService


print("=" * 50)
print("         SURAJ AI AGENT")
print("=" * 50)

print("\nSelect Content Type")
print("1. Long Video")
print("2. Shorts")

choice = input("\nEnter Choice : ")

if choice == "1":

    content_type = "Long Video"

elif choice == "2":

    content_type = "Shorts"

else:

    print("Invalid Choice")
    exit()

topic = input("\nEnter Topic : ")

print("\nResearching...\n")

research_agent = ResearchAgent()

research = research_agent.generate(topic)

print("✅ Research Completed")

print("\nGenerating Content...\n")

content_agent = ContentAgent()

content = content_agent.generate(

    topic=topic,

    content_type=content_type,

    research=research

)

print("✅ Content Generated")

print("\nGenerated Script\n")
print("-" * 60)

print(content.script)

print("-" * 60)

print("\nSaving To Notion...\n")

notion = NotionService()

notion.save_content(content)

print("✅ Saved Successfully")

print("\nWorkflow Status")

print("-------------------------")
print("Research     ✅")
print("Content      ✅")
print("Parser       ✅")
print("Notion       ✅")
print("-------------------------")

print("\nStatus : Draft")

print("\n✅ Done")