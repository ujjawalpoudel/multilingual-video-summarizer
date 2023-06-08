from pytube import YouTube


def get_metadata_video(url):
    # * Get Data from Youtube
    yt = YouTube(url)

    youtube_metadata = {
        "title": yt.title,
        "thumbnail": yt.thumbnail_url,
        "description": yt.description,
        "author": yt.author,
        "length": yt.length,
        "rating": yt.rating,
        "views": yt.views,
        "keywords": yt.keywords,
        "video_id": yt.video_id,
        "publish_date": yt.publish_date,
        "video_url": yt.watch_url,
    }

    # Define the

    return youtube_metadata
