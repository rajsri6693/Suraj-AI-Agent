from google import genai

from config import Config

from prompts.research_prompt import RESEARCH_PROMPT

from utils.retry import retry


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=Config.GEMINI_API_KEY
        )

    @retry
    def generate(self, prompt):

        response = self.client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt

        )

        return response.text

    @retry
    def generate_research(self, topic, news):

        prompt = f"""
{RESEARCH_PROMPT}

Topic:
{topic}

Latest News:

{news}

"""

        response = self.client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt

        )

        return response.text