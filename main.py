# Import Python modules
import certifi
import ssl
from flask import Flask, send_from_directory
from mongoengine import connect
from flask_cors import CORS
import os

# Import user-defined functions
from app.route.youtube.summarize_video import summarize_module
from config import host_uri

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Initialize Flask API
app = Flask(__name__)

# Enable CORS for all origins and allow all methods and headers
CORS(app)

# Define the path to the static directory
static_dir = os.path.join(app.root_path, 'static')

# Initialize base Flask API
@app.route("/")
def hello_world():
    return "Hello, User!"

# Serve files from the static directory
@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory(static_dir, filename)

# Register Blueprint
app.register_blueprint(summarize_module, url_prefix="/youtube")

# Define the MongoDB connection
connect(host=host_uri, tlsCAFile=certifi.where())

# Run API Server
if __name__ == "__main__":
    app.run(debug=True)
