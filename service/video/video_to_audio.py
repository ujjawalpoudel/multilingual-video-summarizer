from moviepy.editor import VideoFileClip


def convert_to_audio(video_path):
    print("video_path", video_path)
    videoclip = VideoFileClip(video_path)

    # Split Video_path to get the audio_path
    audio_path = video_path.split(".")[0] + ".wav"

    audioclip = videoclip.audio

    audioclip.write_audiofile(
        audio_path, codec="pcm_s16le", ffmpeg_params=["-ar", "16000"]
    )

    return audio_path
