import os

from services.gemini_service import GeminiService
from services.image_service import ImageService


class ThumbnailAgent:

    def __init__(self):

        self.gemini = GeminiService()

        self.image = ImageService()

    def generate(

        self,

        content

    ):

        print("\nGenerating Thumbnail Prompt...\n")

        prompt = f"""
You are an expert YouTube Thumbnail Designer.

Generate ONE thumbnail prompt.

Topic:
{content.topic}

Script:
{content.script}

Rules:

- Bright Colors
- High CTR
- Large Human Face
- Emotional Expression
- Background related to topic
- Cinematic Lighting
- Ultra Realistic
- 16:9
- No Watermark

Return ONLY the prompt.
"""

        thumbnail_prompt = self.gemini.generate(

            prompt

        ).strip()

        content.thumbnail_prompt = thumbnail_prompt

        filename = (

            content.topic

            .lower()

            .replace(" ", "_")

            + ".png"

        )

        output = os.path.join(

            "output",

            "thumbnails",

            filename

        )

        self.image.generate(

            thumbnail_prompt,

            output

        )

        content.thumbnail_path = output

        print("\n✅ Thumbnail Generated")

        return content