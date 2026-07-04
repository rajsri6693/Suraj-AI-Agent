import os

from config import Config
from services.subtitle_service import SubtitleService


class SubtitleAgent:

    def __init__(self):

        self.subtitle_service = SubtitleService(

            Config.SUBTITLE_OUTPUT

        )

    def generate(self, content):

        filename = content.topic.lower()

        filename = filename.replace(" ", "_")

        filename = "".join(

            c for c in filename

            if c.isalnum() or c == "_"

        )

        subtitle_path = self.subtitle_service.generate(

            filename,

            content.script

        )

        content.subtitle_path = subtitle_path

        print("✅ Subtitle Generated")

        return subtitle_path