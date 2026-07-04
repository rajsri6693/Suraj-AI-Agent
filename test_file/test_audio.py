import os

from config import Config
from services.ffmpeg_service import FFmpegService


service = FFmpegService()

video = os.path.join(

    Config.FINAL_VIDEO_OUTPUT,

    "nifty_50_today.mp4"

)

audio = os.path.join(

    Config.AUDIO_OUTPUT,

    "nifty_50_today.mp3"

)

output = os.path.join(

    Config.FINAL_VIDEO_OUTPUT,

    "nifty_50_today_voice.mp4"

)

service.add_audio(

    video,

    audio,

    output

)

print()

print("Voice Added Successfully")

print(output)