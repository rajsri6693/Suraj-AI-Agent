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

            content.script,

            content.audio_duration

        )

        content.subtitle_path = subtitle_path

        # Lock in the narration text now, before the visual planner
        # generates any Pexels keywords - this is the baseline the
        # keyword-leak guard compares against later.
        content.script_snapshot = content.script

        with open(subtitle_path, "r", encoding="utf-8") as f:
            content.subtitle_snapshot = f.read()

        print("✅ Subtitle Generated")

        return subtitle_path