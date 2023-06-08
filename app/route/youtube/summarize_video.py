# * Built-in modules
import json

# * Third-party modules
from flask import Blueprint, request
from mongoengine import DoesNotExist
from pytube import YouTube


# * Custom modules
from utils.response_utils import response
from service.video.youtube_metadata import get_metadata_video
from service.video.download_youtube_video import download_video
from service.video.video_to_audio import convert_to_audio


# * Define Blueprint for API Routes
summarize_module = Blueprint("summarize_module", __name__)


# * Define API Route for Login
@summarize_module.route("/summarize", methods=["POST"])
def get_summarize():
    try:
        # * Get Data from Frontend
        data = json.loads(request.data)
        url = data["url"]

        # * Get MetaData from Youtube
        metadata = get_metadata_video(url)

        # * Download Video from Youtube and get the save path
        video_path = download_video(url)

        # * Get Audio from given Video
        audio_path = convert_to_audio(video_path)

        return response(
            200,
            {
                "msg": "Successfully Extracted Video",
                "metadata": metadata,
                "video_path": video_path,
                "audio_path": audio_path,
            },
        )

    except DoesNotExist:
        return response(401, {"msg": "Invalid URL Address"})
