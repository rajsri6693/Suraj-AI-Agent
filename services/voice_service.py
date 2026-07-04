import asyncio
import os
import re

import edge_tts

from config import Config


class VoiceService:

    def __init__(self):

        self.voice = Config.VOICE_NAME

        self.output_dir = os.path.join("output", "audio")

        os.makedirs(self.output_dir, exist_ok=True)

    # ---------------------------------
    # Clean File Name
    # ---------------------------------

    def _clean_filename(self, text):

        text = text.lower()

        text = re.sub(r"[^a-z0-9]+", "_", text)

        return text.strip("_")

    # ---------------------------------
    # Clean Script For Better TTS
    # ---------------------------------

    def _clean_script(self, script):

        if not script:
            return ""

        # Remove markdown
        script = script.replace("*", "")
        script = script.replace("#", "")
        script = script.replace("`", "")

        # Finance words
        replacements = {

            "Nifty 50": "Nifty Fifty",
            "NIFTY 50": "Nifty Fifty",

            "BankNifty": "Bank Nifty",
            "BANKNIFTY": "Bank Nifty",

            "Sensex": "Sensex",

            "NASDAQ": "Nasdaq",

            "Dow Jones": "Dow Jones",

            "S&P 500": "S and P Five Hundred",

            "%": " percent ",

            "₹": " rupees ",

            "...": ".",

            "..": ".",

            "—": ",",

            "-": " "

        }

        for old, new in replacements.items():

            script = script.replace(old, new)

        # Remove multiple spaces
        script = re.sub(r"\s+", " ", script)

        # Better pauses
        script = script.replace(". ", ".\n")
        script = script.replace("? ", "?\n")
        script = script.replace("! ", "!\n")

        script = script.strip()

        return script

    # ---------------------------------
    # Generate Voice
    # ---------------------------------

    async def _generate(self, script, output_file):

        communicate = edge_tts.Communicate(

            text=script,

            voice=self.voice,

            rate="+15%",

            pitch="+0Hz",

            volume="+0%"

        )

        await communicate.save(output_file)

    # ---------------------------------
    # Public Function
    # ---------------------------------

    def generate_audio(self, topic, script):

        filename = self._clean_filename(topic)

        output_file = os.path.join(

            self.output_dir,

            f"{filename}.mp3"

        )

        script = self._clean_script(script)

        print("\n===================================")
        print("Generating Voice")
        print("===================================")
        print()
        print("Voice :", self.voice)
        print("Rate  : +15%")
        print("Topic :", topic)
        print("Length:", len(script))
        print("Output:", output_file)
        print()

        try:

            asyncio.run(

                self._generate(

                    script,

                    output_file

                )

            )

        except Exception as e:

            raise RuntimeError(

                f"Edge TTS Error : {e}"

            )

        if not os.path.exists(output_file):

            raise FileNotFoundError(

                f"Audio file not created : {output_file}"

            )

        size = os.path.getsize(output_file)

        print("Audio Size :", round(size / 1024, 2), "KB")
        print("✅ Voice Generated")
        print()

        return output_file