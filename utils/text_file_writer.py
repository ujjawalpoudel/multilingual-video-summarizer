import os


def save_text_to_file(text_content, video_id):
    """
    Save the provided text content to a file.

    Args:
        text_content (str): The text content to be saved to the file.
        video_id (str): The ID of the video associated with the text.

    Returns:
        str: The file path where the text is saved.
    """
    # Define the directory to save the text files
    output_dir = os.path.join(os.getcwd(), "static", "text_files")

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create the file path for the text file
    file_path = os.path.join(output_dir, f"{video_id}.txt")

    # Open the file in write mode ('w') to either create a new file or overwrite an existing one
    with open(file_path, "w") as file:
        file.write(text_content)

    return file_path
