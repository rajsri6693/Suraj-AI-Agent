from dataclasses import dataclass


@dataclass
class Content:

    topic: str

    content_type: str

    script: str

    title: str

    description: str

    tags: str

    thumbnail_prompt: str

    status: str = "Draft"

    page_id: str = ""

    audio_path: str = ""

    audio_duration: float = 0.0

    # Narration/subtitle text captured right after voice + subtitle
    # generation, before the visual planner invents any Pexels
    # keywords. Used to tell a real keyword injection apart from a
    # keyword that coincidentally shares words with the (independently
    # written) narration.
    script_snapshot: str = ""

    subtitle_snapshot: str = ""

    subtitle_path: str = ""

    video_path: str = ""

    thumbnail_path: str = ""

    youtube_url: str = ""