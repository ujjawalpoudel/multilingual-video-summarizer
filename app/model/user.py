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
