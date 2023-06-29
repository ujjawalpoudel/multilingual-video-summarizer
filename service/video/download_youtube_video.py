import os
from yt_dlp import YoutubeDL


def download_video_as_mp3(url):
    # Set the save path directory
    output_dir = os.path.join(os.getcwd(), "static")

    # Create the save path directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Set the download options  for the video
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
    }

    with YoutubeDL(ydl_opts) as ydl:
        # Download the video
        info_dict = ydl.extract_info(url, download=True)
        # video_title = info_dict.get('title', 'video')

        # Get the save path of the audio
        file_path = ydl.prepare_filename(info_dict)

        # Change the file extension to .mp3
        mp3_file_path = os.path.splitext(file_path)[0] + ".mp3"

    return mp3_file_path
