from dataclasses import dataclass


@dataclass
class Scene:

    scene: int

    sentence: str

    keyword: str

    search_query: str

    video_type: str

    mood: str

    duration: float

    video_path: str = ""