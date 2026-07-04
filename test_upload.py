from services.youtube_service import YouTubeService

service = YouTubeService()

service.upload_video(

    video_file="output/final_videos/nifty_50_today_final.mp4",

    title="Nifty 50 Today 🚀",

    description="Uploaded by Suraj AI Agent",

    tags=[
        "Nifty",
        "Stock Market",
        "AI"
    ],

    privacy="private"

)