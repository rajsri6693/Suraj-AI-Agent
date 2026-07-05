from services.gemini_service import GeminiService
from utils.scene_parser import SceneParser
from prompts.visual_planner_prompt import VISUAL_PLANNER_PROMPT


class VisualPlannerAgent:

    def __init__(self):

        self.gemini = GeminiService()

    # --------------------------------------
    # MAIN ENTRY
    # --------------------------------------

    def generate(self, content):

        prompt = f"""
{VISUAL_PLANNER_PROMPT}

SCRIPT

{content.script}
"""

        response = self.gemini.generate(prompt)

        scenes = SceneParser.parse(response)

        # Total video duration must always equal the actual narration
        # duration, never a hardcoded Shorts/Long Video guess.
        total_duration = getattr(content, "audio_duration", 0) or (
            60 if getattr(content, "content_type", "Shorts").lower() == "shorts" else 180
        )

        scenes = self._balance_duration(scenes, total_duration)

        return scenes

    # --------------------------------------
    # DURATION ENGINE (scenes sum to narration duration)
    # --------------------------------------

    def _balance_duration(self, scenes, total_duration):

        if not scenes:
            return scenes

        n = len(scenes)

        # Weights system
        weights = []

        for i in range(n):

            if i == 0:
                weights.append(1.5)   # hook
            elif i == n - 1:
                weights.append(1.3)   # ending
            else:
                weights.append(1.0)

        total_weight = sum(weights)

        allocated = 0.0

        for i, scene in enumerate(scenes):

            ratio = weights[i] / total_weight

            duration = max(3.0, total_duration * ratio)

            scene.duration = round(duration, 2)

            allocated += scene.duration

        # Correct rounding drift on the last scene so the sum of
        # scene durations matches the narration duration exactly
        drift = total_duration - allocated

        scenes[-1].duration = round(

            max(3.0, scenes[-1].duration + drift),

            2

        )

        return scenes