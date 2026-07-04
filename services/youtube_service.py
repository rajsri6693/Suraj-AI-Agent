import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from config import Config


class YouTubeService:

    SCOPES = [
        "https://www.googleapis.com/auth/youtube.upload"
    ]

    def __init__(self):

        self.youtube = self.authenticate()

    def authenticate(self):

        print("\n========== DEBUG ==========")
        print("Client Secret :", Config.YOUTUBE_CLIENT_SECRET)
        print("Exists        :", os.path.exists(Config.YOUTUBE_CLIENT_SECRET))
        print("Absolute Path :", os.path.abspath(Config.YOUTUBE_CLIENT_SECRET))
        print("===========================\n")

        creds = None

        if (
            Config.YOUTUBE_TOKEN
            and os.path.exists(Config.YOUTUBE_TOKEN)
        ):

            creds = Credentials.from_authorized_user_file(
                Config.YOUTUBE_TOKEN,
                self.SCOPES
            )

        if not creds or not creds.valid:

            if creds and creds.expired and creds.refresh_token:

                creds.refresh(
                    Request()
                )

            else:

                client_secret = os.path.abspath(
                    Config.YOUTUBE_CLIENT_SECRET
                )

                flow = InstalledAppFlow.from_client_secrets_file(
                    client_secret,
                    self.SCOPES
                )

                creds = flow.run_local_server(
                    port=0
                )

            with open(
                Config.YOUTUBE_TOKEN,
                "w",
                encoding="utf-8"
            ) as token:

                token.write(
                    creds.to_json()
                )

        return build(
            "youtube",
            "v3",
            credentials=creds
        )

    # ---------------------------------
    # Upload Video
    # ---------------------------------

    def upload_video(

        self,

        video_file,

        title,

        description,

        tags=None,

        privacy="private",

        category="22"

    ):

        if not os.path.exists(video_file):

            raise FileNotFoundError(video_file)

        if tags is None:

            tags = []

        body = {

            "snippet": {

                "title": title,

                "description": description,

                "tags": tags,

                "categoryId": category

            },

            "status": {

                "privacyStatus": privacy,

                "selfDeclaredMadeForKids": False

            }

        }

        media = MediaFileUpload(

            video_file,

            resumable=True

        )

        request = self.youtube.videos().insert(

            part="snippet,status",

            body=body,

            media_body=media

        )

        print("\nUploading Video...\n")

        response = None

        while response is None:

            status, response = request.next_chunk()

            if status:

                print(

                    f"Progress : {int(status.progress() * 100)}%"

                )

        print("\n===================================")
        print("Video Uploaded Successfully")
        print("===================================\n")

        print("Video ID :", response["id"])
        print("Link : https://youtu.be/" + response["id"])

        return response["id"]

            # ---------------------------------
    # Upload Thumbnail
    # ---------------------------------

    def upload_thumbnail(

        self,

        video_id,

        thumbnail_file

    ):

        if not os.path.exists(thumbnail_file):

            raise FileNotFoundError(

                thumbnail_file

            )

        media = MediaFileUpload(

            thumbnail_file,

            mimetype="image/png"

        )

        self.youtube.thumbnails().set(

            videoId=video_id,

            media_body=media

        ).execute()

        print()

        print("===================================")
        print("Thumbnail Uploaded Successfully")
        print("===================================")
        print()

        return True