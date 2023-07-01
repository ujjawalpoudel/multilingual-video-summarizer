# Built-in modules
import json

# Third-party modules
from flask import Blueprint, request
from flask_cors import cross_origin

# Custom modules
from utils.response_utils import response
from service.video.audio_to_text import convert_audio_to_text

# Define the blueprint for the audio-to-text functionality
audio_to_text_blueprint = Blueprint("audio_to_text", __name__)


# Define the API route for converting audio to text
@audio_to_text_blueprint.route("/convert", methods=["POST"])
@cross_origin()
def convert_audio_to_text_route():
    try:
        # Get data from the frontend
        data = json.loads(request.data)
        file_path = data["file_path"]

        # Convert audio to text
        text = convert_audio_to_text(file_path)

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
