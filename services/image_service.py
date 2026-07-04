import os
import requests
from urllib.parse import quote


class ImageService:

    BASE_URL = "https://image.pollinations.ai/prompt/"

    def generate(

        self,

        prompt,

        output_path

    ):

        os.makedirs(

            os.path.dirname(output_path),

            exist_ok=True

        )

        url = self.BASE_URL + quote(prompt)

        print("\nDownloading Thumbnail...\n")

        response = requests.get(

            url,

            timeout=120

        )

        response.raise_for_status()

        with open(

            output_path,

            "wb"

        ) as file:

            file.write(

                response.content

            )

        print("✅ Thumbnail Downloaded")

        return output_path