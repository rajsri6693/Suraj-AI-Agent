from services.gemini_service import GeminiService
from services.research_service import ResearchService
from utils.script_validator import ScriptValidator
from core.quality_engine import QualityEngine

from prompts import (
    SHORTS_SYSTEM_PROMPT,
    LONG_VIDEO_SYSTEM_PROMPT
)


class ScriptAgent:

    def __init__(self):

        self.gemini = GeminiService()
        self.research = ResearchService()
        self.validator = ScriptValidator()

        # ✅ Quality Engine (NEW)
        self.quality = QualityEngine()

    # ---------------------------------
    # Format Research Better
    # ---------------------------------

    def _format_research(self, topic, latest_news):

        if not latest_news:
            return f"No recent updates found for {topic}"

        return f"""
Latest Verified Market Data:
{latest_news}

Focus:
- Use only factual updates
- Avoid outdated information
- Keep narration conversational
"""

    # ---------------------------------
    # Build Prompt
    # ---------------------------------

    def _build_prompt(self, system_prompt, topic, research_summary, content_type):

        return f"""
{system_prompt}

===================================
STRICT INSTRUCTIONS:
===================================

1. Write a HIGH RETENTION YouTube script
2. First 3 seconds MUST be a strong HOOK
3. Use simple spoken Hindi (not formal writing)
4. No timestamps, no markdown, no symbols
5. Avoid robotic tone
6. Use short sentences
7. Keep pacing natural for voiceover

===================================
CONTENT TYPE:
===================================

{content_type}

===================================
VIDEO TARGETS:
===================================

Shorts:
- Duration: 55–60 seconds
- Words: 140–170

Long Video:
- Duration: 2–3 minutes
- Words: 420–520

===================================
TOPIC:
===================================

{topic}

===================================
LATEST RESEARCH:
===================================

{research_summary}

===================================

OUTPUT FORMAT:
Only return:
- Title
- Script
- Description
- Tags
"""

    # ---------------------------------
    # Generate Script
    # ---------------------------------

    def generate(self, topic, content_type):

        print("\n===================================")
        print("Researching Latest News...")
        print("===================================\n")

        latest_news = self.research.get_research(topic)

        print("Generating Research Summary...\n")

        research_summary = self.gemini.generate_research(
            topic,
            latest_news
        )

        system_prompt = SHORTS_SYSTEM_PROMPT if content_type == "Shorts" else LONG_VIDEO_SYSTEM_PROMPT

        prompt = self._build_prompt(
            system_prompt,
            topic,
            research_summary,
            content_type
        )

        print("Generating Script...\n")

        raw_script = self.gemini.generate(prompt)

        print("Validating Script...\n")

        errors = self.validator.validate(raw_script)

        if errors:

            print("Script Validation Failed:", errors)

            return None, errors

        # ---------------------------------
        # ✅ QUALITY ENGINE APPLY
        # ---------------------------------

        print("Applying Quality Engine...\n")

        script = self.quality.process_pro(raw_script)

        print("Script Generated Successfully\n")

        return script, []