import re
import bson


def email_check(email):
    # * Make a regular expression for validating an Email
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def bson_id_check(id):
    # * Check mongo ObjectID is valid.
    if bson.objectid.ObjectId.is_valid(id):
        return True
    else:
        return False
