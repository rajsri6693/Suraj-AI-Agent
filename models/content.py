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

    subtitle_path: str = ""

    video_path: str = ""

    thumbnail_path: str = ""

    youtube_url: str = ""