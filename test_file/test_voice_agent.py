from agents.voice_agent import VoiceAgent
from models.content import Content

content = Content(

    topic="Nifty 50 Today",

    content_type="Shorts",

    script="""
नमस्कार दोस्तों।

आज निफ्टी 50 में शानदार तेजी देखने को मिली।

ऐसी ही अपडेट के लिए चैनल को सब्सक्राइब करें।
""",

    title="",

    description="",

    tags="",

    thumbnail_prompt=""

)

agent = VoiceAgent()

audio = agent.generate(content)

print(audio)