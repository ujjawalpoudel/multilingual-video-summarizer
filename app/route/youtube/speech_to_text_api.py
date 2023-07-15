# Built-in modules
import json

# Third-party modules
from flask import Blueprint, request
from flask_cors import cross_origin

# Custom modules
from app.validator.file_path_validator import FilePathValidator
from utils.response_utils import response
from utils.validation_decorators import pydantic_validation
from service.video.audio_to_text import convert_audio_to_text

# Import DB models
from app.model.vidoe import Video

# Define the blueprint for the audio-to-text functionality
audio_to_text_blueprint = Blueprint("audio_to_text", __name__)


# Define the API route for converting audio to text
@audio_to_text_blueprint.route("/convert", methods=["POST"])
@pydantic_validation(FilePathValidator)
@cross_origin()
def convert_audio_to_text_route():
    try:
        # Get data from the frontend
        data = json.loads(request.data)
        file_path = data["file_path"]
        video_id = data["video_id"]

        # Check if video metadata already exists in DB
        video = Video.objects(video_id=video_id).first()

        # If video object already exists in DB, get text from that and return it
        if video:
            text = video.text
        else:
            # Convert audio to text
            text = convert_audio_to_text(file_path)

            # Update the video metadata
            video.text = text
            video.save()

        # Return a success response with the extracted text
        return response(
            200,
            {
                "message": "Audio successfully converted to text.",
                "text": text,
            },
        )
    except Exception as e:
        # Handle any exceptions and return an error response
        error_message = str(e)
        return response(401, {"message": error_message})
