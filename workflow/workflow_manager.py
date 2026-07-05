from agents.voice_agent import VoiceAgent
from agents.subtitle_agent import SubtitleAgent
from agents.visual_planner_agent import VisualPlannerAgent
from agents.pexels_agent import PexelsAgent
from agents.video_agent import VideoAgent
from agents.thumbnail_agent import ThumbnailAgent

from services.youtube_service import YouTubeService
from services.telegram_service import TelegramService

from core.quality_engine import QualityEngine


class WorkflowManager:

    def __init__(

        self,

        notion_service=None

    ):

        self.notion = notion_service

        self.quality_engine = QualityEngine()

        self.voice_agent = VoiceAgent()

        self.subtitle_agent = SubtitleAgent()

        self.visual_agent = VisualPlannerAgent()

        self.pexels_agent = PexelsAgent()

        self.video_agent = VideoAgent()

        self.thumbnail_agent = ThumbnailAgent()

        self.youtube = YouTubeService()

        self.telegram = TelegramService()

    # ---------------------------------
    # Update Status
    # ---------------------------------

    def update_status(

        self,

        content,

        status

    ):

        if self.notion:

            self.notion.update_status(

                content.page_id,

                status

            )

        print(f"✅ {status}")

    # ---------------------------------
    # Workflow
    # ---------------------------------

    def run(

        self,

        content

    ):

        print()

        print("===================================")

        print("      Starting Workflow")

        print("===================================")

        print()

        # ---------------------------------

        # Approved Narration
        # Strip any inline visual/scene-cue tags (e.g. "[investor
        # panic]") left in the approved script. These are editorial
        # hints for reviewing the script in Notion, not narration -
        # Voice, Subtitle and Video must only ever see clean text.

        # ---------------------------------

        content.script = self.quality_engine.process(content.script)

        # ---------------------------------

        # Voice

        # ---------------------------------

        print("Generating Voice...")

        self.voice_agent.generate(

            content

        )

        self.update_status(

            content,

            "Processing"

        )

        # ---------------------------------

        # Subtitle

        # ---------------------------------

        print()

        print("Generating Subtitle...")

        self.subtitle_agent.generate(

            content

        )

        # ---------------------------------

        # Scene Planner

        # ---------------------------------

        print()

        print("Generating Scene Plan...")

        scenes = self.visual_agent.generate(

            content

        )

        # ---------------------------------

        # Download Videos

        # ---------------------------------

        print()

        print("Downloading Videos...")

        scenes = self.pexels_agent.generate(

            scenes

        )

        # ---------------------------------

        # Render Video

        # ---------------------------------

        print()

        print("Rendering Final Video...")

        self.video_agent.generate(

            content,

            scenes

        )

        print()

        print("Generating Thumbnail...")

        self.thumbnail_agent.generate(

            content

        )
        # ---------------------------------
        # Upload Video
        # ---------------------------------

        print()

        print("Uploading Video...")

        video_id = self.youtube.upload_video(

            video_file=content.video_path,

            title=content.title,

            description=content.description,

            tags=[

                tag.strip()

                for tag in content.tags.split(",")

                if tag.strip()

            ],

            privacy="private"

        )

        content.youtube_url = (

            "https://youtu.be/" + video_id

        )

        # ---------------------------------
        # Upload Thumbnail
        # ---------------------------------

        print()

        print("Uploading Thumbnail...")

        self.youtube.upload_thumbnail(

            video_id,

            content.thumbnail_path

        )

        # ---------------------------------
        # Update Notion
        # ---------------------------------

        if self.notion:

            self.notion.update_video_link(

                content.page_id,

                content.youtube_url

            )

            self.notion.update_status(

                content.page_id,

                "Completed"

            )

        # ---------------------------------
        # Telegram
        # ---------------------------------

        message = f"""
✅ <b>Video Uploaded Successfully</b>

<b>Topic</b>
{content.topic}

<b>Title</b>
{content.title}

<b>YouTube</b>

{content.youtube_url}
"""

        self.telegram.send(

            message

        )

        print()

        print("===================================")

        print("     Workflow Completed")

        print("===================================")

        print()

        return content