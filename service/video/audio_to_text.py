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

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio_file_path)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)

    source_language = max(probs, key=probs.get)
    task = "translate"

    # Transcribe the audio file
    # result = model.transcribe(audio_file_path)
    result = model.transcribe(audio_file_path, task=task, language=source_language)

    # Return the transcribed text
    return result["text"], source_language
