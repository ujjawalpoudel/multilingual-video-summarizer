# Import Python Libraries
import whisper


def convert_audio_to_text(audio_file_path):
    """
    Converts an audio file to a text file.

    Args:
        audio_file_path (str): Path to the audio file.

    Returns:
        str: converted text .
    """

    # Load the Whisper model
    model = whisper.load_model("base")

    # Transcribe the audio file
    result = model.transcribe(audio_file_path)

    # Return the transcribed text
    return result["text"]
