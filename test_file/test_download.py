import os

from config import Config
from services.pexels_service import PexelsService


service = PexelsService(
    Config.PEXELS_API_KEY
)

result = service.search(
    "Indian stock market"
)

url = service.get_best_video(result)

print("\nVideo URL:\n")
print(url)

path = service.download(
    url,
    os.path.join(
        Config.RAW_VIDEO_OUTPUT,
        "market.mp4"
    )
)

print("\nSaved:\n")
print(path)