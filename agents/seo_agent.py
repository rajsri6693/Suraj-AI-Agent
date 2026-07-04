from services.gemini_service import GeminiService


class SEOAgent:

    def __init__(self):

        self.gemini = GeminiService()

    def generate(self, topic, script):

        prompt = f"""

You are a YouTube SEO Expert.

Using the topic and script below generate:

1. Title
2. Description
3. Tags

Rules:

- Title under 70 characters.
- Description 2–3 paragraphs.
- Tags comma separated.
- No clickbait.
- SEO optimized.
- Return only:

TITLE:
...

DESCRIPTION:
...

TAGS:
...

Topic:
{topic}

Script:
{script}

"""

        return self.gemini.generate(prompt)