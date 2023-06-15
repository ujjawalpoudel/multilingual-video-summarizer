# Built-in modules
import json

# Third-party modules
import pytube
from flask import Blueprint, request

# Custom modules
from utils.response_utils import response
from service.video.youtube_metadata import get_video_metadata
from service.video.download_youtube_video import download_video
from service.video.video_to_audio import convert_video_to_audio
from service.video.audio_to_text import convert_audio_to_text

# Define Blueprint for API Routes
summarize_module = Blueprint("summarize_module", __name__)


# Define API Route for Summarizing
@summarize_module.route("/summarize", methods=["POST"])
def get_summarize():
    try:
        # Get data from frontend
        data = json.loads(request.data)
        url = data["url"]

        # Get metadata from YouTube
        metadata = get_video_metadata(url)

        # Download video from YouTube and get the save path
        video_path = download_video(url)

        # Get audio from the given video
        audio_path = convert_video_to_audio(video_path)

        # Get text from the given audio
        text = convert_audio_to_text(audio_path)

        return response(
            200,
            {
                "msg": "Successfully extracted video metadata, audio, and text.",
                "metadata": metadata,
                "video_path": video_path,
                "audio_path": audio_path,
                "text": text,
            },
        )
    except pytube.exceptions.PytubeError as e:
        # Handle PytubeError and return an error response
        error_message = str(e)
        return response(500, {"msg": error_message})

    except Exception as e:
        # Handle other exceptions and return an error response
        error_message = str(e)
        return response(401, {"msg": error_message})
