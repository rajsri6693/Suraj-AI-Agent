from agents.thumbnail_agent import ThumbnailAgent
from models.content import Content


content = Content(

    topic="Nifty 50 Today",

    content_type="Shorts",

    script="""

आज बाजार में शानदार तेजी आई।

निफ्टी 50 ने नया हाई बनाया।

""",

    title="",

    description="",

    tags="",

    thumbnail_prompt="",

    status="Approved"

)

agent = ThumbnailAgent()

content = agent.generate(

    content

)

print()

print("="*50)

print(content.thumbnail_prompt)