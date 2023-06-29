# Built-in modules
import json

# Third-party modules
from flask import Blueprint, request

# Custom modules
from utils.response_utils import response
from service.video.youtube_metadata import get_video_metadata
from service.video.download_youtube_video import download_video_as_mp3
from service.video.audio_to_text import convert_audio_to_text

# Define Blueprint for API Routes
summarize_module = Blueprint("summarize_module", __name__)


# Define API Route for Summarizing
@summarize_module.route("/summarize", methods=["POST"])
def summarize_video():
    try:
        # Get data from frontend
        data = json.loads(request.data)
        url = data["url"]

        # Get metadata from YouTube
        video_metadata = get_video_metadata(url)

        # Download video from YouTube and get the save path
        # video_path = download_video(url)

        # Get audio from the given video
        audio_path = download_video_as_mp3(url)

        # Get text from the given audio
        text = convert_audio_to_text(audio_path)

        return response(
            200,
            {
                "message": "Successfully extracted video metadata, audio, and text.",
                "metadata": video_metadata,
                "audio_path": audio_path,
                "text": text,
            },
        )
    except Exception as e:
        # Handle other exceptions and return an error response
        error_message = str(e)
        return response(401, {"message": error_message})
