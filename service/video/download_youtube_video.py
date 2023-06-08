from pytube import YouTube
import os


def download_video(url):
    # * Get Data from Youtube
    yt = YouTube(url)

    # Get the YouTube video stream with itag 22
    stream = yt.streams.get_by_itag(22)

    # Joining paths
    save_path = os.path.join(os.getcwd(), "static")

    # Create the save path directory if it doesn't exist
    os.makedirs(save_path, exist_ok=True)

    # Download the video to the specified path
    video_path = stream.download(save_path)

    return video_path
