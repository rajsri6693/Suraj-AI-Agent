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

        # ✅ FIX: duration balancing layer
        scenes = self._balance_duration(
            scenes,
            getattr(content, "video_type", "Shorts")
        )

        return scenes

    # --------------------------------------
    # DURATION ENGINE (FIX 34 sec BUG)
    # --------------------------------------

    def _balance_duration(self, scenes, video_type):

        if not scenes:
            return scenes

        # Total duration
        if video_type.lower() == "shorts":
            total = 60
        else:
            total = 180

        n = len(scenes)

        if n == 0:
            return scenes

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

        for i, scene in enumerate(scenes):

            ratio = weights[i] / total_weight

            duration = int(total * ratio)

            # Safety clamp
            duration = max(3, min(duration, 12))

            scene.duration = duration

        return scenes