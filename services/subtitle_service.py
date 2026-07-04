import os
import re


class SubtitleService:

    def __init__(self, output_dir):

        self.output_dir = output_dir

        os.makedirs(output_dir, exist_ok=True)

    # ---------------------------------------
    # Convert Seconds -> SRT Timestamp
    # ---------------------------------------

    def _format_time(self, seconds):

        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        milliseconds = int((seconds - int(seconds)) * 1000)

        return (
            f"{hours:02}:{minutes:02}:{secs:02},"
            f"{milliseconds:03}"
        )

    # ---------------------------------------
    # Generate Subtitle
    # ---------------------------------------

    def generate(self, filename, script):

        # Split sentences

        sentences = re.split(r"[।.!?]\s*", script.strip())

        sentences = [

            s.strip()

            for s in sentences

            if s.strip()

        ]

        current_time = 0.0

        subtitle_lines = []

        for index, sentence in enumerate(sentences, start=1):

            word_count = len(sentence.split())

            duration = max(

                2.0,

                word_count / 2.8

            )

            start = self._format_time(current_time)

            end = self._format_time(

                current_time + duration

            )

            subtitle_lines.append(str(index))

            subtitle_lines.append(

                f"{start} --> {end}"

            )

            subtitle_lines.append(sentence)

            subtitle_lines.append("")

            current_time += duration

        output_path = os.path.join(

            self.output_dir,

            f"{filename}.srt"

        )

        with open(

            output_path,

            "w",

            encoding="utf-8"

        ) as f:

            f.write(

                "\n".join(subtitle_lines)

            )

        return output_path