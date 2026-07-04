import re
import random


class ThumbnailEngine:

    """
    Thumbnail CTR Engine V1

    Purpose:
    - Maximize YouTube CTR
    - Convert script → thumbnail idea
    - Create emotional + financial hooks
    """

    def __init__(self):

        self.emotions = [
            "Shock",
            "Fear",
            "Greed",
            "Urgency",
            "Excitement",
            "Confusion"
        ]

        self.arrows = ["⬇", "🔻", "📉", "⚠", "🔥"]

    # --------------------------------------
    # MAIN ENTRY
    # --------------------------------------

    def generate(self, title, script):

        emotion = self._detect_emotion(script)

        number = self._extract_number(script)

        keyword = self._extract_keyword(title, script)

        headline = self._build_headline(emotion, number, keyword)

        design = self._design_elements(emotion)

        return {
            "headline": headline,
            "emotion": emotion,
            "keyword": keyword,
            "design": design
        }

    # --------------------------------------
    # EMOTION DETECTION
    # --------------------------------------

    def _detect_emotion(self, text):

        text = text.lower()

        if any(word in text for word in ["crash", "fall", "loss", "down"]):
            return "Fear"

        if any(word in text for word in ["profit", "gain", "rise", "boom"]):
            return "Greed"

        if any(word in text for word in ["urgent", "breaking"]):
            return "Urgency"

        return random.choice(self.emotions)

    # --------------------------------------
    # NUMBER EXTRACTION
    # --------------------------------------

    def _extract_number(self, text):

        numbers = re.findall(r"\d+", text)

        return numbers[0] if numbers else None

    # --------------------------------------
    # KEYWORD EXTRACTION
    # --------------------------------------

    def _extract_keyword(self, title, script):

        keywords = [

            "Nifty",
            "Stock Market",
            "Crash",
            "Profit",
            "Loss",
            "Bank Nifty",
            "Sensex"

        ]

        combined = title + " " + script

        for k in keywords:

            if k.lower() in combined.lower():
                return k

        return "Market"

    # --------------------------------------
    # HEADLINE BUILDER
    # --------------------------------------

    def _build_headline(self, emotion, number, keyword):

        arrow = random.choice(self.arrows)

        if number:

            return f"{emotion} {arrow} {keyword} {number}!"

        return f"{emotion} {arrow} {keyword} ALERT!"

    # --------------------------------------
    # DESIGN ELEMENTS
    # --------------------------------------

    def _design_elements(self, emotion):

        return {

            "background": self._bg_color(emotion),

            "text_color": "white",

            "font_weight": "bold",

            "overlay": "high_contrast",

            "elements": [
                "red_arrow",
                "chart_down",
                "face_reaction"
            ]

        }

    # --------------------------------------
    # BACKGROUND COLOR LOGIC
    # --------------------------------------

    def _bg_color(self, emotion):

        mapping = {

            "Fear": "red_black",
            "Greed": "green_gold",
            "Urgency": "red_flash",
            "Shock": "yellow_red",
            "Excitement": "blue_neon",
            "Confusion": "purple_dark"
        }

        return mapping.get(emotion, "black_red")