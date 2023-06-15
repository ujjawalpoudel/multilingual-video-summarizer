# Standard library imports
import datetime

# Third-party imports
from mongoengine import Document, ValidationError
from mongoengine.fields import DateTimeField, StringField, EmailField, IntField


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


class User(DefaultAttributes, Document):
    """
    User model with attributes such as fullname, email, and password.
    """

    fullname = StringField(max_length=200, required=True, validation=validate_name)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)


class Video(DefaultAttributes, Document):
    """
    Video model with attributes such as title, url, author, length, video_id,
    publish_date, video_path, audio_path, and text.
    """

    title = StringField(max_length=200, required=True, validation=validate_name)
    url = StringField(required=True, unique=True)
    author = StringField(max_length=200, required=True, validation=validate_name)
    length = IntField(required=True)
    video_id = StringField(required=True, unique=True)
    publish_date = DateTimeField(required=True)
    video_path = StringField(required=True, unique=True)
    audio_path = StringField(required=True, unique=True)
    text = StringField(required=True, unique=True)
