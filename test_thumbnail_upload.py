from services.youtube_service import YouTubeService

service = YouTubeService()

video_id = "MWtqRjIbNyk"

thumbnail = "output/thumbnails/nifty_50_today.png"

service.upload_thumbnail(

    video_id,

    thumbnail

)