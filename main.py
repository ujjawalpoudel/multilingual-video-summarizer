# Import Python modules
import certifi
import ssl
from flask import Flask, send_from_directory
from mongoengine import connect
from flask_cors import CORS
import os

# Import user-defined functions
from app.route.youtube.youtube_metadata_api import video_metadata_blueprint
from app.route.youtube.file_download_api import file_download_blueprint
from app.route.youtube.speech_to_text_api import audio_to_text_blueprint
from config import host_uri

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Initialize Flask API
app = Flask(__name__)

# Enable CORS for all origins and allow all methods and headers
CORS(app)

# Define the path to the static directory
static_dir = os.path.join(app.root_path, "static")


# Initialize base Flask API
@app.route("/")
def hello_world():
    return "Hello, User!"


# Serve files from the static directory
@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory(static_dir, filename)


# Register Blueprint for API Routes
app.register_blueprint(video_metadata_blueprint, url_prefix="/video")
app.register_blueprint(file_download_blueprint, url_prefix="/video")
app.register_blueprint(audio_to_text_blueprint, url_prefix="/audio")

# Define the MongoDB connection
print(host_uri)
connect(host=host_uri, tlsCAFile=certifi.where())

# Run API Server
if __name__ == "__main__":
    app.run(debug=True)
