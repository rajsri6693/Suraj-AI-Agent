from services.gemini_service import GeminiService
from utils.parser import AIOutputParser
from models.content import Content

from prompts.content_prompt import CONTENT_PROMPT


class ContentAgent:

    def __init__(self):

        self.gemini = GeminiService()

    def generate(self, topic, content_type, research):

        prompt = CONTENT_PROMPT.format(

            topic=topic,

            content_type=content_type,

            research=research

        )

        output = self.gemini.generate(prompt)

        result = AIOutputParser.parse(output)

        return Content(

            topic=topic,

            content_type=content_type,

            script=result["script"],

            title=result["title"],

            description=result["description"],

            tags=result["tags"],

            thumbnail_prompt=result["thumbnail"]

        )