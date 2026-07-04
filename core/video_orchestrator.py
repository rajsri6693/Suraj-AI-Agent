from agents.script_agent import ScriptAgent
from agents.visual_planner_agent import VisualPlannerAgent
from utils.subtitle_engine import SubtitleEngine
from core.thumbnail_engine import ThumbnailEngine
from core.quality_engine import QualityEngine


class VideoOrchestrator:

    def __init__(self):

        self.script_agent = ScriptAgent()
        self.visual_agent = VisualPlannerAgent()

        self.subtitle_engine = SubtitleEngine()
        self.thumbnail_engine = ThumbnailEngine()

        self.quality_engine = QualityEngine()

    # --------------------------------------
    # MAIN PIPELINE
    # --------------------------------------

    def run(self, topic, content_type="Shorts"):

        print("\n===================================")
        print("VIDEO PIPELINE STARTED")
        print("===================================\n")

        # 1. SCRIPT GENERATION
        script, errors = self.script_agent.generate(topic, content_type)

        if errors:
            print("Script Error:", errors)
            return None

        # 2. QUALITY FIX
        script = self.quality_engine.process_pro(script)

        # 3. VISUAL PLANNING
        scenes = self.visual_agent.generate(script)

        # 4. SUBTITLES
        duration = 60 if content_type == "Shorts" else 180

        subtitles = self.subtitle_engine.generate(script, duration)

        # 5. THUMBNAIL
        thumbnail = self.thumbnail_engine.generate(
            topic,
            script
        )

        print("\n===================================")
        print("PIPELINE COMPLETED")
        print("===================================\n")

        return {

            "script": script,
            "scenes": scenes,
            "subtitles": subtitles,
            "thumbnail": thumbnail
        }