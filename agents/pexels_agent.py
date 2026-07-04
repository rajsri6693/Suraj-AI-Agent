import os

from config import Config
from services.pexels_service import PexelsService


class PexelsAgent:

    def __init__(self):

        self.service = PexelsService(

            Config.PEXELS_API_KEY

        )

    def generate(self, scenes):

        print("\nDownloading Videos...\n")

        for scene in scenes:

            print(

                f"Scene {scene.scene} : {scene.search_query}"

            )

            result = self.service.search(

                scene.search_query

            )

            url = self.service.get_best_video(

                result

            )

            if not url:

                print(

                    "❌ No Video Found"

                )

                continue

            filename = f"scene_{scene.scene}.mp4"

            output_path = os.path.join(

                Config.RAW_VIDEO_OUTPUT,

                filename

            )

            self.service.download(

                url,

                output_path

            )

            scene.video_path = output_path

            print(

                "✅ Downloaded"

            )

        return scenes