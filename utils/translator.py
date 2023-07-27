import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Hugging Face API token from the environment variable
hugging_face_api_token = os.getenv("HUGGING_FACE_API_TOKEN")


def translate_text(text_to_translate, target_language, source_language="en"):
    """
    Translates the input text to the specified target language using the Hugging Face translation API.

    Args:
        text_to_translate (str): The input text to be translated.
        target_language (str): The target language code to which the text will be translated.
        source_language (str, optional): The source language code of the input text (default is "en").

    Returns:
        str: The translated text in the target language, or None if the translation failed.
    """
    # API endpoint for translation
    API_URL = f"https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-{source_language}-{target_language}"

    # Authorization token for API access
    token = f"Bearer {hugging_face_api_token}"
    headers = {"Authorization": token}

    # Prepare the payload with the input text
    payload = {"inputs": text_to_translate}

    # Send the POST request to the translation API
    response = requests.post(API_URL, headers=headers, json=payload)

    # Parse the response and extract the translated text
    if response.status_code == 200:
        output = response.json()
        translated_text = output[0].get("translation_text", "")
        return translated_text
    else:
        print("Translation failed. Status code:", response.status_code)
        return None
