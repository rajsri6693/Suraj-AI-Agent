import re
from datetime import datetime


class QualityEngine:
    """
    Suraj AI Quality Engine V1

    This engine improves AI generated scripts before:

    • Voice Generation
    • Subtitle Generation
    • Video Planning

    Pipeline

    Raw Script
            ↓
    Basic Cleaning
            ↓
    Finance Formatting
            ↓
    Hook Optimization
            ↓
    Sentence Optimization
            ↓
    TTS Optimization
            ↓
    Final Script
    """

    def __init__(self):

        self.today = datetime.now()

    # ==========================================================
    # PUBLIC ENTRY
    # ==========================================================

    def process(self, script: str):

        if not script:
            return ""

        script = self.basic_clean(script)

        script = self.remove_markdown(script)

        script = self.normalize_spaces(script)

        script = self.fix_quotes(script)

        script = self.remove_duplicate_punctuation(script)

        script = self.fix_line_breaks(script)

        script = self.remove_empty_lines(script)

        return script.strip()

    # ==========================================================
    # BASIC CLEAN
    # ==========================================================

    def basic_clean(self, text):

        text = text.replace("\r", "")

        text = text.replace("\t", " ")

        text = text.replace(" ", " ")

        return text

    # ==========================================================
    # REMOVE MARKDOWN
    # ==========================================================

    def remove_markdown(self, text):

        markdown = [

            "#",
            "*",
            "`",
            "_",
            ">"

        ]

        for item in markdown:

            text = text.replace(item, "")

        return text

    # ==========================================================
    # NORMALIZE SPACES
    # ==========================================================

    def normalize_spaces(self, text):

        text = re.sub(r"[ ]+", " ", text)

        return text

    # ==========================================================
    # FIX QUOTES
    # ==========================================================

    def fix_quotes(self, text):

        text = text.replace("“", '"')

        text = text.replace("”", '"')

        text = text.replace("’", "'")

        text = text.replace("‘", "'")

        return text

    # ==========================================================
    # REMOVE DUPLICATE PUNCTUATION
    # ==========================================================

    def remove_duplicate_punctuation(self, text):

        while ".." in text:

            text = text.replace("..", ".")

        while "??" in text:

            text = text.replace("??", "?")

        while "!!" in text:

            text = text.replace("!!", "!")

        while ",," in text:

            text = text.replace(",,", ",")

        return text

    # ==========================================================
    # FIX LINE BREAKS
    # ==========================================================

    def fix_line_breaks(self, text):

        text = text.replace(". ", ".\n")

        text = text.replace("? ", "?\n")

        text = text.replace("! ", "!\n")

        return text

    # ==========================================================
    # REMOVE EMPTY LINES
    # ==========================================================

    def remove_empty_lines(self, text):

        lines = []

        for line in text.split("\n"):

            line = line.strip()

            if line:

                lines.append(line)

        return "\n".join(lines)
    
    # ==========================================================
    # FINANCE FORMATTER
    # ==========================================================

    def finance_formatter(self, text):

        replacements = {

            "Nifty 50": "Nifty Fifty",

            "NIFTY 50": "Nifty Fifty",

            "BANKNIFTY": "Bank Nifty",

            "BankNifty": "Bank Nifty",

            "Sensex": "Sensex",

            "NASDAQ": "Nasdaq",

            "S&P 500": "S and P Five Hundred",

            "Dow Jones": "Dow Jones",

            "FII": "Foreign Institutional Investors",

            "DII": "Domestic Institutional Investors",

            "IPO": "I P O",

            "ETF": "E T F"

        }

        for old, new in replacements.items():

            text = text.replace(old, new)

        return text

    # ==========================================================
    # FORMAT CURRENCY
    # ==========================================================

    def currency_formatter(self, text):

        text = re.sub(

            r"₹\s*([\d,]+)",

            r"\1 rupees",

            text

        )

        text = re.sub(

            r"\$\s*([\d,]+)",

            r"\1 dollars",

            text

        )

        return text

    # ==========================================================
    # FORMAT PERCENT
    # ==========================================================

    def percent_formatter(self, text):

        text = re.sub(

            r"(\d+(\.\d+)?)%",

            r"\1 percent",

            text

        )

        return text

    # ==========================================================
    # REMOVE DATE REFERENCES
    # ==========================================================

    def remove_date_reference(self, text):

        months = [

            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"

        ]

        for month in months:

            pattern = rf"\d+\s+{month}"

            text = re.sub(

                pattern,

                "today",

                text,

                flags=re.IGNORECASE

            )

        return text

    # ==========================================================
    # REMOVE URLS
    # ==========================================================

    def remove_urls(self, text):

        text = re.sub(

            r"http\S+",

            "",

            text

        )

        text = re.sub(

            r"www\S+",

            "",

            text

        )

        return text

    # ==========================================================
    # REMOVE EMOJIS
    # ==========================================================

    def remove_emojis(self, text):

        emoji_pattern = re.compile(

            "["
            "\U0001F600-\U0001F64F"
            "\U0001F300-\U0001F5FF"
            "\U0001F680-\U0001F6FF"
            "\U0001F1E0-\U0001F1FF"
            "]+",

            flags=re.UNICODE

        )

        return emoji_pattern.sub("", text)

    # ==========================================================
    # TTS OPTIMIZER
    # ==========================================================

    def tts_optimizer(self, text):

        text = text.replace("...", ".")

        text = text.replace("..", ".")

        text = text.replace("—", ",")

        text = text.replace(";", ".")

        text = text.replace(":", ",")

        text = re.sub(

            r"\s+",

            " ",

            text

        )

        text = text.replace(". ", ".\n")

        text = text.replace("? ", "?\n")

        text = text.replace("! ", "!\n")

        return text

    # ==========================================================
    # PROCESS V2
    # ==========================================================

    def process_v2(self, script):

        script = self.process(script)

        script = self.finance_formatter(script)

        script = self.currency_formatter(script)

        script = self.percent_formatter(script)

        script = self.remove_date_reference(script)

        script = self.remove_urls(script)

        script = self.remove_emojis(script)

        script = self.tts_optimizer(script)

        return script.strip()

    # ==========================================================
    # HOOK OPTIMIZER
    # ==========================================================

    def optimize_hook(self, text):

        lines = text.split("\n")

        if not lines:
            return text

        first = lines[0].strip()

        weak_starts = [

            "namaste",
            "hello",
            "hi",
            "welcome",
            "aaj hum",
            "is video me",
            "friends",
            "dosto"

        ]

        lower = first.lower()

        for item in weak_starts:

            if lower.startswith(item):

                lines.pop(0)

                break

        if not lines:
            return text

        hook = lines[0].strip()

        if len(hook) < 35:

            hook = "Aaj market me ek bada badlav dekhne ko mila. " + hook

            lines[0] = hook

        return "\n".join(lines)

    # ==========================================================
    # REMOVE DUPLICATE SENTENCES
    # ==========================================================

    def remove_duplicate_sentences(self, text):

        result = []

        seen = set()

        for sentence in text.split("\n"):

            s = sentence.strip()

            if not s:
                continue

            key = s.lower()

            if key in seen:
                continue

            seen.add(key)

            result.append(s)

        return "\n".join(result)

    # ==========================================================
    # SENTENCE OPTIMIZER
    # ==========================================================

    def optimize_sentences(self, text):

        text = re.sub(

            r"\s+",

            " ",

            text

        )

        text = text.replace(" ,", ",")

        text = text.replace(" .", ".")

        text = text.replace(" ?", "?")

        text = text.replace(" !", "!")

        text = text.replace(",.", ".")

        text = text.replace("..", ".")

        return text.strip()

    # ==========================================================
    # READABILITY SCORE
    # ==========================================================

    def readability_score(self, text):

        words = len(text.split())

        sentences = max(

            1,

            text.count(".") +

            text.count("?") +

            text.count("!")

        )

        avg = words / sentences

        if avg <= 12:

            return "Excellent"

        if avg <= 18:

            return "Good"

        if avg <= 24:

            return "Average"

        return "Hard"

    # ==========================================================
    # FINAL PRODUCTION PIPELINE
    # ==========================================================

    def process_pro(self, script):

        script = self.process_v2(script)

        script = self.optimize_hook(script)

        script = self.remove_duplicate_sentences(script)

        script = self.optimize_sentences(script)

        score = self.readability_score(script)

        print("\n===================================")
        print("Quality Engine")
        print("===================================")
        print("Readability :", score)
        print("Characters  :", len(script))
        print("Words       :", len(script.split()))
        print("===================================\n")

        return script

    # ==========================================================
    # CALL SUPPORT
    # ==========================================================

    def __call__(self, script):

        return self.process_pro(script)