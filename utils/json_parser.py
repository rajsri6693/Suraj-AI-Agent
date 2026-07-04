import json
import re


class JsonParser:

    @staticmethod
    def parse(text):

        if not text:
            return None

        try:

            text = text.strip()

            # Remove Markdown code fences

            text = re.sub(

                r"^```json\s*",

                "",

                text,

                flags=re.IGNORECASE

            )

            text = re.sub(

                r"^```",

                "",

                text

            )

            text = re.sub(

                r"```$",

                "",

                text

            )

            text = text.strip()

            # Try normal JSON first

            return json.loads(text)

        except Exception:

            try:

                # Extract JSON array

                start = text.find("[")

                end = text.rfind("]")

                if start != -1 and end != -1:

                    return json.loads(

                        text[start:end + 1]

                    )

                # Extract JSON object

                start = text.find("{")

                end = text.rfind("}")

                if start != -1 and end != -1:

                    return json.loads(

                        text[start:end + 1]

                    )

            except Exception:

                return None

        return None