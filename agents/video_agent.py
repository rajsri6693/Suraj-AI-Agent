import os

from services.ffmpeg_service import FFmpegService
from models.scene import Scene
from models.content import Content
from config import Config


class VideoAgent:

    def __init__(self):

        self.ffmpeg = FFmpegService()

    def generate(

        self,

        content: Content,

        scenes: list[Scene]

    ):

        print("\nGenerating Final Video...\n")

        normalized_clips = []

        # -----------------------------
        # Normalize Every Scene
        # -----------------------------

        for scene in scenes:

            output = os.path.join(

                Config.NORMALIZED_VIDEO_OUTPUT,

                f"scene_{scene.scene}.mp4"

            )

            self.ffmpeg.normalize_and_trim(

                scene.video_path,

                output,

                scene.duration

            )

            normalized_clips.append(output)

        # -----------------------------
        # Merge
        # -----------------------------

        merged_video = os.path.join(

            Config.FINAL_VIDEO_OUTPUT,

            "merged.mp4"

        )

        self.ffmpeg.merge_clips(

            normalized_clips,

            merged_video

        )

        # -----------------------------
        # Add Voice
        # -----------------------------

        voice_video = os.path.join(

            Config.FINAL_VIDEO_OUTPUT,

            f"{content.topic.lower().replace(' ', '_')}_voice.mp4"

        )

        self.ffmpeg.add_audio(

            merged_video,

            content.audio_path,

            voice_video

        )

        # -----------------------------
        # Burn Subtitle
        # -----------------------------

        subtitle_file = os.path.join(

            Config.SUBTITLE_OUTPUT,

            f"{content.topic.lower().replace(' ', '_')}.srt"

        )

        final_video = os.path.join(

            Config.FINAL_VIDEO_OUTPUT,

            f"{content.topic.lower().replace(' ', '_')}.mp4"

        )

        self.ffmpeg.burn_subtitles(

            voice_video,

            subtitle_file,

            final_video

        )

        content.video_path = final_video

        print("✅ Final Video Ready")

        return final_video