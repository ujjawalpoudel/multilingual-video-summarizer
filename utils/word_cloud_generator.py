import os
from wordcloud import WordCloud


def generate_word_cloud_and_save(text_content, video_id):
    """
    Generate a Word Cloud from the given text and save it as an image file.

    Parameters:
        text_content (str): The input text for generating the Word Cloud.
        video_id (str): The unique ID of the video.

    Returns:
        str: The file path of the saved Word Cloud image.
    """

    # Create a WordCloud object
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(
        text_content
    )

    # Set the directory to save the Word Cloud image
    output_dir = os.path.join(os.getcwd(), "static", "word_clouds")

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create the file path for the Word Cloud image
    filename = os.path.join(output_dir, f"{video_id}.png")

    # Save the Word Cloud as an image file
    wordcloud.to_file(filename)

    return filename
