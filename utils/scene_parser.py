import json

from models.scene import Scene


class SceneParser:

    @staticmethod
    def parse(text):

        data = json.loads(text)

        scenes = []

        for item in data:

            scenes.append(

                Scene(

                    scene=item["scene"],

                    sentence=item["sentence"],

                    keyword=item["keyword"],

                    search_query=item["search_query"],

                    video_type=item["video_type"],

                    mood=item["mood"],

                    duration=float(item["duration"])

                )

            )

        return scenes