import os
from pytube import YouTube


def download_video(url):
    """
    Downloads a YouTube video using the provided URL and returns the path to the downloaded video.

    Args:
        url (str): The URL of the YouTube video to download.

    Returns:
        str: The path to the downloaded video file.
    """
    # Get data from YouTube
    yt = YouTube(url)

    # Get the YouTube video stream with itag 22 (720p resolution)
    stream = yt.streams.get_by_itag(22)

    # Set the save path directory
    save_path = os.path.join(os.getcwd(), "static")

    # Create the save path directory if it doesn't exist
    os.makedirs(save_path, exist_ok=True)

    # Download the video to the specified path
    video_path = stream.download(save_path)

    return video_path
