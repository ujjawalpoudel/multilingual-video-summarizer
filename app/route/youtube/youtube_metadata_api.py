# Third-party modules
from flask import Blueprint, request
from flask_cors import cross_origin

# Custom modules
from app.validator.url_validator import URLValidator
from utils.response_utils import response
from utils.validation_decorators import pydantic_validation
from service.video.youtube_metadata import get_video_metadata

# Import DB models
from app.model.video import Video

# Define Blueprint for API Routes
video_metadata_blueprint = Blueprint("video_metadata", __name__)


# Define API Route for getting video metadata
@video_metadata_blueprint.route("/metadata", methods=["GET"])
@pydantic_validation(URLValidator)
@cross_origin()
def get_video_metadata_route():
    try:
        # Get data from frontend
        video_url = request.args.get("url")

        # Get metadata from YouTube
        video_metadata = get_video_metadata(video_url)

        # Save metadata to DB
        video = Video(**video_metadata)
        video.save()

        return response(
            200,
            {
                "message": "Successfully extracted video metadata.",
                "metadata": video_metadata,
            },
        )
    except Exception as e:
        # Handle exceptions and return an error response
        error_message = str(e)
        return response(401, {"message": error_message})
