import re
import math


class SubtitleEngine:

    """
    V2 Subtitle Engine

    Features:
    - Clean subtitles
    - Word grouping
    - Timing distribution
    - TikTok style pacing support
    """

    def __init__(self):

        pass

    # --------------------------------------
    # MAIN ENTRY
    # --------------------------------------

    def generate(self, script, total_duration=60):

        sentences = self._split_sentences(script)

        subtitles = []

        n = len(sentences)

        if n == 0:
            return []

        # duration per sentence (base)
        base_time = total_duration / n

        current_time = 0.0

        for sentence in sentences:

            sentence = sentence.strip()

            if not sentence:
                continue

            words = sentence.split()

            word_count = len(words)

            # dynamic timing
            duration = self._calculate_duration(
                base_time,
                word_count
            )

            subtitle = {
                "text": sentence,
                "start": round(current_time, 2),
                "end": round(current_time + duration, 2),
                "words": self._build_word_timings(
                    words,
                    current_time,
                    duration
                )
            }

            subtitles.append(subtitle)

            current_time += duration

        return subtitles

    # --------------------------------------
    # SENTENCE SPLIT
    # --------------------------------------

    def _split_sentences(self, text):

        text = re.sub(r"\s+", " ", text)

        sentences = re.split(r"[.!?]\s*", text)

        return [s for s in sentences if s.strip()]

    # --------------------------------------
    # DURATION CALCULATOR
    # --------------------------------------

    def _calculate_duration(self, base_time, word_count):

        # reading speed adjustment
        speed_factor = 0.35  # seconds per word

        dynamic_time = word_count * speed_factor

        return max(1.2, min(base_time + dynamic_time, 6))

    # --------------------------------------
    # WORD TIMING (TikTok style)
    # --------------------------------------

    def _build_word_timings(self, words, start_time, duration):

        if not words:
            return []

        word_duration = duration / len(words)

        result = []

        current = start_time

        for word in words:

            result.append({
                "word": word,
                "start": round(current, 2),
                "end": round(current + word_duration, 2)
            })

            current += word_duration

        return result