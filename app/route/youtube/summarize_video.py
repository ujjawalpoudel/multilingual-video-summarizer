# Built-in modules
import json

# Third-party modules
from flask import Blueprint, request
from flask_cors import cross_origin

# Custom modules
from utils.response_utils import response
from service.video.youtube_metadata import get_video_metadata
from service.video.download_youtube_video import download_video_as_mp3
from service.video.audio_to_text import convert_audio_to_text

# Define Blueprint for API Routes
summarize_module = Blueprint("summarize_module", __name__)


# Define API Route for getting video metadata
@summarize_module.route("/video_meta", methods=["POST"])
@cross_origin()
def get_video_metadata_route():
    try:
        # Get data from frontend
        data = json.loads(request.data)
        url = data["url"]

        # Get metadata from YouTube
        video_metadata = get_video_metadata(url)

        return response(
            200,
            {
                "message": "Successfully extracted video metadata.",
                "metadata": video_metadata,
            },
        )
    except Exception as e:
        # Handle other exceptions and return an error response
        error_message = str(e)
        return response(401, {"message": error_message})


# Define API Route for getting audio file URL
@summarize_module.route("/audio_file", methods=["POST"])
@cross_origin()
def get_audio_file_route():
    try:
        # Get data from frontend
        data = json.loads(request.data)
        url = data["url"]

        # Download video from YouTube and get the audio file URL
        audio_path = download_video_as_mp3(url)

        return response(
            200,
            {
                "message": "Successfully obtained audio file URL.",
                "audio_path": audio_path,
            },
        )
    except Exception as e:
        # Handle other exceptions and return an error response
        error_message = str(e)
        return response(401, {"message": error_message})


# Define API Route for summarizing video
@summarize_module.route("/summarize", methods=["POST"])
@cross_origin()
def summarize_video():
    try:
        # Get data from frontend
        data = json.loads(request.data)
        audio_path = data["url"]

        # Get text from the given audio
        text = convert_audio_to_text(audio_path)

        return response(
            200,
            {
                "message": "Successfully extracted video metadata, audio, and text.",
                "text": text,
            },
        )
    except Exception as e:
        # Handle other exceptions and return an error response
        error_message = str(e)
        return response(401, {"message": error_message})
