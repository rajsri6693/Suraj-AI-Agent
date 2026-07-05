import os
import subprocess

from config import Config


class FFmpegService:

    def __init__(self):

        self.ffmpeg = Config.FFMPEG_PATH

        self.ffprobe = Config.FFPROBE_PATH

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
    # Get Media Duration (ffprobe)
    # ---------------------------------

    def get_duration(self, path):

        command = [

            self.ffprobe,

            "-v",

            "error",

            "-show_entries",

            "format=duration",

            "-of",

            "default=noprint_wrappers=1:nokey=1",

            path

        ]

        result = subprocess.run(

            command,

            check=True,

            capture_output=True,

            text=True

        )

        return float(result.stdout.strip())

    # ---------------------------------
    # Extend Last Frame (freeze-pad)
    # ---------------------------------

    def extend_last_frame(

        self,

        input_video,

        output_video,

        extra_seconds

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

            "-vf",

            f"tpad=stop_mode=clone:stop_duration={extra_seconds}",

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

        output_video,

        duration=None

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

            Config.AUDIO_CODEC

        ]

        if duration:

            # Video has already been padded to at least this length,
            # so clamping to it never cuts the narration short.
            command += ["-t", str(duration)]

        else:

            command.append("-shortest")

        command.append(output_video)

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