from pytube import YouTube

# Import Custom Modules
from app.model.video import Video


def get_video_metadata(url):
    """
    Get metadata of a YouTube video using its URL.

    Args:
        url (str): The URL of the YouTube video.

    Returns:
        dict: A dictionary containing the metadata of the video.
    """
    # Create a YouTube object with the given URL
    yt = YouTube(url)

    # Extract relevant metadata from the YouTube object
    youtube_metadata = {
        "title": yt.title,
        # "thumbnail": yt.thumbnail_url,
        # "description": yt.description,
        "author": yt.author,
        "length": yt.length,
        # "rating": yt.rating,
        # "views": yt.views,
        # "keywords": yt.keywords,
        "video_id": yt.video_id,
        "publish_date": yt.publish_date,
        "video_url": yt.watch_url,
    }

    # Check if the video already exists in the database
    video = Video.objects(video_id=yt.video_id).first()

    # If video object is None, then the video does not exist in the database
    if video == None:
        # Save all information to the database
        video = Video(**youtube_metadata)
        video.save()

    return youtube_metadata
