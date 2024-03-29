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
from utils.word_cloud_generator import generate_word_cloud_and_save
from utils.text_file_writer import save_text_to_file
from utils.translator import translate_text

# Import DB models
from app.model.video import Video
from utils.file_id_extractor import extract_id_from_file_path

# Define the blueprint for the audio-to-text functionality
audio_to_text_blueprint = Blueprint("audio_to_text", __name__)


# Define the API route for converting audio to text
@audio_to_text_blueprint.route("/convert", methods=["POST"])
# @pydantic_validation(FilePathValidator)
@cross_origin()
def convert_audio_to_text_route():
    try:
        # Get data from the frontend
        data = json.loads(request.data)
        file_path = data["file_path"]

        # Extract the video ID from the file path
        video_id = extract_id_from_file_path(file_path)

        # Check if video metadata already exists in DB
        video = Video.objects(video_id=video_id).first()

        # Check if video object has text attribute
        if hasattr(video, "text") and video.text is not None:
            text = video.text
        else:
            # Convert audio to text
            text, source_language = convert_audio_to_text(file_path)

            # Define a target language for translation
            target_language = "en"

            # Update the video metadata
            video.text = text
            video.source_language = source_language

            # Check if the source language and target language are different
            if source_language != target_language:
                # Translate the text to English
                video.source_text = translate_text(
                    text, source_language, target_language
                )
            else:
                video.source_text = text
            video.save()

        # Generate a word cloud from the extracted text
        word_cloud_path = generate_word_cloud_and_save(text, video_id)

        # Save the extracted text to a file
        text_file_path = save_text_to_file(text, video_id)

        # Convert video to json
        video_json = video.get_json(
            return_fields=[
                "title",
                "video_url",
                "author",
                "video_id",
                "text",
                "source_language",
                "source_text",
                "id",
            ]
        )

        # Add information about the word cloud, text file and message to the video json
        video_json["word_cloud_path"] = word_cloud_path
        video_json["text_file_path"] = text_file_path
        video_json["message"] = "Audio successfully converted to text."

        # Return a success response with the extracted text
        return response(
            200,
            video_json,
        )
    except Exception as e:
        # Handle any exceptions and return an error response
        error_message = str(e)
        return response(401, {"message": error_message})
