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
    # Group Words Into 2-4 Word Chunks
    # ---------------------------------------

    def _group_words(self, words):

        groups = []

        i = 0

        n = len(words)

        while i < n:

            remaining = n - i

            if remaining <= 4:

                groups.append(words[i:])

                break

            size = 3

            # Avoid leaving a trailing single-word group
            if remaining - size == 1:

                size = 2

            groups.append(words[i:i + size])

            i += size

        return groups

    # ---------------------------------------
    # Generate Subtitle
    # ---------------------------------------

    def generate(self, filename, script, total_duration=None):

        # Strip sentence punctuation, keep plain words only
        clean_script = re.sub(r"[।.!?,]", " ", script.strip())

        words = [w for w in clean_script.split() if w]

        if not words:
            words = []

        groups = self._group_words(words)

        word_count = len(words)

        if total_duration and word_count:
            word_duration = total_duration / word_count
        else:
            # Fallback pacing when narration duration is unknown
            word_duration = 1 / 2.8

        current_time = 0.0

        subtitle_lines = []

        for index, group in enumerate(groups, start=1):

            duration = max(

                0.5,

                word_duration * len(group)

            )

            start = self._format_time(current_time)

            end = self._format_time(

                current_time + duration

            )

            # 2-4 words, single line - never a full sentence
            text = " ".join(group)

            subtitle_lines.append(str(index))

            subtitle_lines.append(

                f"{start} --> {end}"

            )

            subtitle_lines.append(text)

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