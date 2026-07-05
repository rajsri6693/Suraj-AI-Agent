import os

from services.voice_service import VoiceService
from services.ffmpeg_service import FFmpegService


class VoiceAgent:

    def __init__(self):

        self.voice_service = VoiceService()

        self.ffmpeg = FFmpegService()

    def generate(self, content):

        print("\n===================================")
        print("Generating Voice")
        print("===================================\n")

        print("Topic :", content.topic)

        if content.script:
            print("Script Length :", len(content.script))
        else:
            print("Script Length : 0")
            raise ValueError("Script is empty.")

        print("Audio Before :", content.audio_path)

        audio_path = self.voice_service.generate_audio(

            topic=content.topic,

            script=content.script

        )

        print("Generated Audio :", audio_path)

        print("File Exists :", os.path.exists(audio_path))

        if not os.path.exists(audio_path):

            raise FileNotFoundError(

                f"Audio file not found : {audio_path}"

            )

        content.audio_path = audio_path

        content.audio_duration = self.ffmpeg.get_duration(audio_path)

        print("Narration Duration :", content.audio_duration)

        print("✅ Voice Generated")

        return audio_path