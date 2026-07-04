import os
import requests


class PexelsService:

    BASE_URL = "https://api.pexels.com/videos/search"

    def __init__(self, api_key):

        self.api_key = api_key

    # ---------------------------------------
    # Search Videos
    # ---------------------------------------

    def search(self, query, per_page=5):

        headers = {

            "Authorization": self.api_key

        }

        params = {

            "query": query,

            "per_page": per_page

        }

        response = requests.get(

            self.BASE_URL,

            headers=headers,

            params=params,

            timeout=30

        )

        if response.status_code == 401:

            raise Exception(

                "Invalid Pexels API Key."

            )

        response.raise_for_status()

        return response.json()

    # ---------------------------------------
    # Get Best Video URL
    # ---------------------------------------

    def get_best_video(self, result):

        videos = result.get(

            "videos",

            []

        )

        if not videos:

            return None

        video = videos[0]

        files = video.get(

            "video_files",

            []

        )

        if not files:

            return None

        best = max(

            files,

            key=lambda f: (

                f.get("width", 0),

                f.get("height", 0)

            )

        )

        return best.get("link")

    # ---------------------------------------
    # Download Video
    # ---------------------------------------

    def download(

        self,

        url,

        output_path

    ):

        if not url:

            return None

        os.makedirs(

            os.path.dirname(output_path),

            exist_ok=True

        )

        response = requests.get(

            url,

            stream=True,

            timeout=60

        )

        response.raise_for_status()

        with open(

            output_path,

            "wb"

        ) as file:

            for chunk in response.iter_content(

                chunk_size=8192

            ):

                if chunk:

                    file.write(chunk)

        return output_path

