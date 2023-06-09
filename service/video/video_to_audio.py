from moviepy.editor import VideoFileClip


def convert_video_to_audio(video_path):
    """
    Converts a video file to an audio file.

    Args:
        video_path (str): Path to the video file.

    Returns:
        str: Path to the converted audio file.
    """
    videoclip = VideoFileClip(video_path)

    # Split video_path to get the audio_path
    audio_path = video_path.split(".")[0] + ".wav"

    audioclip = videoclip.audio

    # Write the audio file
    audioclip.write_audiofile(
        audio_path, codec="pcm_s16le", ffmpeg_params=["-ar", "16000"]
    )

    return audio_path
