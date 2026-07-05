import os

from services.ffmpeg_service import FFmpegService
from models.scene import Scene
from models.content import Content
from config import Config


class VideoAgent:

    def __init__(self):

        self.ffmpeg = FFmpegService()

    # ---------------------------------
    # Guard: Pexels search keywords must
    # never leak into narration/subtitles
    # ---------------------------------

    def _assert_no_keyword_leak(self, content, scenes):

        banned_terms = []

        for scene in scenes:

            if scene.keyword:
                banned_terms.append(scene.keyword.strip().lower())

            if scene.search_query:
                banned_terms.append(scene.search_query.strip().lower())

        banned_terms = [t for t in banned_terms if t]

        if not banned_terms:
            return

        # The narration/subtitles are already locked in (voiced and
        # written to disk) before the visual planner ever invents these
        # Pexels search terms - see SubtitleAgent, which snapshots both
        # right after generation. A real leak means a banned term shows
        # up in the narration/subtitles that was NOT already there
        # beforehand, i.e. the application injected it afterwards.
        #
        # A term that was already present before the keyword existed is
        # just topical overlap (e.g. a finance script naturally saying
        # "worried investor", which also happens to be a Pexels search
        # keyword for that scene) - that is not a leak and must never
        # raise here.

        script_before = (content.script_snapshot or content.script or "").lower()
        script_now = (content.script or "").lower()

        for term in banned_terms:

            if term in script_now and term not in script_before:

                raise ValueError(

                    f"Pexels keyword leaked into narration script: '{term}'"

                )

        subtitle_now = ""

        if content.subtitle_path and os.path.exists(content.subtitle_path):

            with open(

                content.subtitle_path,

                "r",

                encoding="utf-8"

            ) as f:

                subtitle_now = f.read().lower()

        if subtitle_now:

            subtitle_before = (content.subtitle_snapshot or subtitle_now).lower()

            for term in banned_terms:

                if term in subtitle_now and term not in subtitle_before:

                    raise ValueError(

                        f"Pexels keyword leaked into subtitles: '{term}'"

                    )

    def generate(

        self,

        content: Content,

        scenes: list[Scene]

    ):

        print("\nGenerating Final Video...\n")

        self._assert_no_keyword_leak(content, scenes)

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
        # Ensure Video Never Ends Before Narration
        # (extend the last visual instead of cutting audio)
        # -----------------------------

        narration_duration = content.audio_duration or self.ffmpeg.get_duration(

            content.audio_path

        )

        merged_duration = self.ffmpeg.get_duration(merged_video)

        if merged_duration < narration_duration - 0.05:

            extended_video = os.path.join(

                Config.FINAL_VIDEO_OUTPUT,

                "merged_extended.mp4"

            )

            self.ffmpeg.extend_last_frame(

                merged_video,

                extended_video,

                narration_duration - merged_duration

            )

            merged_video = extended_video

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

            voice_video,

            duration=narration_duration

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