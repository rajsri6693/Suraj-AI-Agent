import os
import subprocess

from config import Config


class FFmpegService:

    def __init__(self):

        self.ffmpeg = Config.FFMPEG_PATH

    # ---------------------------------
    # Run FFmpeg Command
    # ---------------------------------

    def _run(self, command):

        print("\nRunning FFmpeg Command:\n")
        print(" ".join(command))
        print()

        subprocess.run(
            command,
            check=True
        )

    # ---------------------------------
    # Normalize + Trim
    # ---------------------------------

    def normalize_and_trim(

        self,

        input_video,

        output_video,

        duration

    ):

        os.makedirs(

            os.path.dirname(output_video),

            exist_ok=True

        )

        command = [

            self.ffmpeg,

            "-y",

            "-i",

            input_video,

            "-t",

            str(duration),

            "-vf",

            (
                f"scale={Config.VIDEO_WIDTH}:{Config.VIDEO_HEIGHT}:"
                "force_original_aspect_ratio=increase,"
                f"crop={Config.VIDEO_WIDTH}:{Config.VIDEO_HEIGHT},"
                f"fps={Config.VIDEO_FPS}"
            ),

            "-c:v",

            Config.VIDEO_CODEC,

            "-preset",

            Config.VIDEO_PRESET,

            "-pix_fmt",

            Config.PIXEL_FORMAT,

            "-an",

            output_video

        ]

        self._run(command)

        return output_video

    # ---------------------------------
    # Merge Clips
    # ---------------------------------

    def merge_clips(

        self,

        clips,

        output_path

    ):

        if not clips:

            raise ValueError("No clips provided.")

        os.makedirs(

            os.path.dirname(output_path),

            exist_ok=True

        )

        list_file = os.path.join(

            os.path.dirname(output_path),

            "clips.txt"

        )

        with open(

            list_file,

            "w",

            encoding="utf-8"

        ) as f:

            for clip in clips:

                f.write(

                    f"file '{os.path.abspath(clip)}'\n"

                )

        command = [

            self.ffmpeg,

            "-y",

            "-f",

            "concat",

            "-safe",

            "0",

            "-i",

            list_file,

            "-c",

            "copy",

            output_path

        ]

        self._run(command)

        os.remove(list_file)

        return output_path

    # ---------------------------------
    # Add Audio
    # ---------------------------------

    def add_audio(

        self,

        input_video,

        audio_file,

        output_video

    ):

        os.makedirs(

            os.path.dirname(output_video),

            exist_ok=True

        )

        command = [

            self.ffmpeg,

            "-y",

            "-i",

            input_video,

            "-i",

            audio_file,

            "-c:v",

            "copy",

            "-c:a",

            Config.AUDIO_CODEC,

            "-shortest",

            output_video

        ]

        self._run(command)

        return output_video

    # ---------------------------------
    # Burn Subtitles
    # ---------------------------------

    def burn_subtitles(

        self,

        input_video,

        subtitle_file,

        output_video

    ):

        os.makedirs(

            os.path.dirname(output_video),

            exist_ok=True

        )

        subtitle_path = os.path.abspath(subtitle_file)

        subtitle_path = subtitle_path.replace("\\", "/")

        if ":" in subtitle_path:

            drive = subtitle_path[0]

            subtitle_path = drive + "\\:" + subtitle_path[2:]

        filter_string = f"subtitles='{subtitle_path}'"

        command = [

            self.ffmpeg,

            "-y",

            "-i",

            input_video,

            "-vf",

            filter_string,

            "-c:v",

            Config.VIDEO_CODEC,

            "-preset",

            Config.VIDEO_PRESET,

            "-pix_fmt",

            Config.PIXEL_FORMAT,

            "-c:a",

            "copy",

            output_video

        ]

        self._run(command)

        return output_video