# Standard library imports
import datetime

# Third-party imports
from mongoengine import Document, ValidationError
from mongoengine.fields import DateTimeField, StringField, IntField


def validate_name(name):
    """
    Validate the name to ensure it has at least 2 characters.
    """
    if len(name) < 2:
        raise ValidationError("Name must have at least 2 characters")


class DefaultAttributes:
    """
    Base class for models with default attributes.
    """

    meta = {"allow_inheritance": True}
    creation_date = DateTimeField()
    modified_date = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        """
        Override the save method to set the creation and modification dates.
        """
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(DefaultAttributes, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        """
        Override the update method to update the modification date.
        """
        self.modified_date = datetime.datetime.now()
        return super(DefaultAttributes, self).save(*args, **kwargs)


class Video(DefaultAttributes, Document):
    """
    Video model with attributes such as title, url, author, length, video_id,
    publish_date, video_path, audio_path, and text.
    """

    title = StringField(validation=validate_name)
    video_url = StringField(unique=True)
    author = StringField(validation=validate_name)
    length = IntField()
    video_id = StringField(unique=True, required=True)
    publish_date = DateTimeField()
    video_path = StringField()
    audio_path = StringField()
    text = StringField()
    source_language = StringField()
    source_text = StringField()

    def get_json(self, return_fields=None):
        """
        Returns a dictionary representation of the Video object, including specified return fields.

        Args:
            return_fields (list, optional): A list of field names to be included in the output.
                                            If None, all fields will be returned. (default is None)

        Returns:
            dict: A dictionary containing the specified fields and their values.
        """
        output = {
            "title": self.title,
            "video_url": self.video_url,
            "author": self.author,
            "video_id": self.video_id,
            "text": self.text,
            "source_language": self.source_language,
            "source_text": self.source_text,
            "id": str(self.id),
        }

        if return_fields is not None:
            # Filter the output to include only specified fields
            output = {
                field: value
                for field, value in output.items()
                if field in return_fields
            }

        return output
