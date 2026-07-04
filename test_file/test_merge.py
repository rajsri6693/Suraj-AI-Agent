import os

from config import Config
from services.ffmpeg_service import FFmpegService


service = FFmpegService()

clips = [

    os.path.join(

        Config.RAW_VIDEO_OUTPUT,

        "scene_1.mp4"

    ),

    os.path.join(

        Config.RAW_VIDEO_OUTPUT,

        "scene_2.mp4"

    )

]

output = os.path.join(

    Config.FINAL_VIDEO_OUTPUT,

    "merged.mp4"

)

service.merge_clips(

    clips,

    output

)

print()

print("Merged Successfully")

print(output)