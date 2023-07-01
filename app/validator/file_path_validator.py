import pydantic
import os

# TODO: We have to change this validation after deploy code in server.


def is_valid_file_path(file_path: str):
    """
    Check if the given file path is valid.

    Args:
        file_path (str): The file path to be checked.

    Returns:
        bool: True if the file path is valid, False otherwise.
    """
    try:
        # Checking if the path exists
        if not os.path.exists(file_path):
            return False

        # Checking if the path is a file
        if not os.path.isfile(file_path):
            return False

        return True

    except OSError:
        return False


class FilePathValidator(pydantic.BaseModel, extra=pydantic.Extra.forbid):
    """
    Pydantic model for validating file paths.
    """

    file_path: str

    @pydantic.validator("file_path")
    @classmethod
    def validate_file_path(cls, file_path: str):
        """
        Validate the provided file path.

        Args:
            file_path (str): The file path to be validated.

        Returns:
            str: The validated file path.

        Raises:
            ValueError: If the file path is not valid.
        """
        is_valid_path = is_valid_file_path(file_path)
        if is_valid_path:
            return file_path
        else:
            message = f"The provided file path '{file_path}' is not a valid file path."
            raise ValueError(message)
