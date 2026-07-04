from dotenv import load_dotenv
import os

load_dotenv()


class Config:

    # ==========================
    # API KEYS
    # ==========================

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    NOTION_TOKEN = os.getenv("NOTION_TOKEN")
    NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

    PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

    YOUTUBE_CLIENT_SECRET = os.getenv("YOUTUBE_CLIENT_SECRET")

    YOUTUBE_TOKEN = os.getenv("YOUTUBE_TOKEN")

    # ==========================
    # APP SETTINGS
    # ==========================

    APPROVAL_CHECK_INTERVAL = 30

    MAX_RETRIES = 3

    VOICE_PROVIDER = "edge"

    VOICE_NAME = "hi-IN-SwaraNeural"

    LOG_LEVEL = "INFO"

    DEFAULT_LANGUAGE = "Hindi"

    DEFAULT_CONTENT_TYPE = "Shorts"

    # ==========================
    # OUTPUT PATHS
    # ==========================

    AUDIO_OUTPUT = "output/audio"

    VIDEO_OUTPUT = "output/video"

    THUMBNAIL_OUTPUT = "output/thumbnails"

    SUBTITLE_OUTPUT = "output/subtitles"

    RAW_VIDEO_OUTPUT = "output/raw_videos"

    FINAL_VIDEO_OUTPUT = "output/final_videos"

    FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"

    FFPROBE_PATH = r"C:\ffmpeg\bin\ffprobe.exe"

    NORMALIZED_VIDEO_OUTPUT = "output/normalized_videos"

        # ==========================
    # VIDEO SETTINGS
    # ==========================

    VIDEO_WIDTH = 1080
    VIDEO_HEIGHT = 1920
    VIDEO_FPS = 30

    VIDEO_CODEC = "libx264"

    AUDIO_CODEC = "aac"

    VIDEO_PRESET = "fast"

    PIXEL_FORMAT = "yuv420p"