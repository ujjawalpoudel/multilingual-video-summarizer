def extract_id_from_file_path(file_path):
    """
    Extracts the ID from the given file path.

    Args:
        file_path (str): The path of the file containing the ID.

    Returns:
        str: The extracted ID from the file path.
    """
    # Split the file path by / and take the last part (the file name).
    file_name = file_path.split("/")[-1]

    # Split the file name by dot and take the first part (the ID).
    id = file_name.split(".")[0]

    return id
