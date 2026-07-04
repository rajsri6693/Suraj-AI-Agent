from services.gemini_service import GeminiService
from utils.prompt_loader import PromptLoader


class ScriptService:

    def __init__(self):

        self.gemini = GeminiService()

    def generate_script(self, topic, content_type):

        system_prompt = PromptLoader.load(
            "system_prompt.txt"
        )

        if content_type == "Long":

            content_prompt = PromptLoader.load(
                "long_video_prompt.txt"
            )

        else:

            content_prompt = PromptLoader.load(
                "shorts_prompt.txt"
            )

        final_prompt = f"""

{system_prompt}

{content_prompt}

Topic:

{topic}

"""

        return self.gemini.generate(final_prompt)