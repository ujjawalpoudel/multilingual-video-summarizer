# * Import Python Module
import certifi
from flask import Flask
from mongoengine import connect

# * Import User Defined Functions
from app.route.youtube.summarize_video import summarize_module

from config import host_uri

# Disable SSL certificate verification
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# * Initialize Flask API
app = Flask(__name__)


# * Initialize Base Flask API
@app.route("/")
def hello_world():
    return "Hello, User!"


# * Register Blueprint
app.register_blueprint(summarize_module, url_prefix="/youtube")

# * Define the MongoDB connection
connect(
    host=host_uri,
    tlsCAFile=certifi.where(),
)


# * Run API Server
if __name__ == "__main__":
    app.run(debug=True)
