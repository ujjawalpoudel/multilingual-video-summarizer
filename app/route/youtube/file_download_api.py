# Built-in modules
import json

# Third-party modules
from flask import Blueprint, request
from flask_cors import cross_origin

# Custom modules
from app.validator.url_validator import URLValidator
from utils.response_utils import response
from utils.validation_decorators import pydantic_validation
from service.video.download_youtube_video import download_video_as_mp3

# Define Blueprint for API Routes
file_download_blueprint = Blueprint("file_download", __name__)


@file_download_blueprint.route("/download", methods=["POST"])
@cross_origin()
def download_file():
    try:
        # Get data from the request body
        data = json.loads(request.data)
        url = data["url"]

        # Download the video as MP3 file
        file_path = download_video_as_mp3(url)

        return response(
            200,
            {
                "message": "File downloaded successfully.",
                "file_path": file_path,
            },
        )
    except Exception as e:
        # Handle exceptions and return an error response
        error_message = str(e)
        return response(401, {"message": error_message})
