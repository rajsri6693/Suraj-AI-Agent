import os

from config import Config
from services.ffmpeg_service import FFmpegService


service = FFmpegService()

video = os.path.join(
    Config.FINAL_VIDEO_OUTPUT,
    "nifty_50_today_voice.mp4"
)

subtitle = os.path.join(
    Config.SUBTITLE_OUTPUT,
    "nifty_50_today.srt"
)

output = os.path.join(
    Config.FINAL_VIDEO_OUTPUT,
    "nifty_50_today_final.mp4"
)

service.burn_subtitles(
    video,
    subtitle,
    output
)

print()
print("=" * 35)
print("Subtitle Burned Successfully")
print("=" * 35)
print()
print(output)