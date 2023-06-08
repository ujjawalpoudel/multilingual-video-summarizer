# * Import Python Module
import json
from mongoengine.errors import ValidationError, OperationError
from mongoengine.errors import ValidationError as MongoValidationError
from mongoengine.errors import DoesNotExist as NotFoundError
from mongoengine.errors import OperationError
from pydantic import ValidationError

# * Import User Defined Functions
from utils.response_utils import response
from utils.generic_error import GenericError


def error_handler(func):
    """Decorator used to catch certain types of Exceptions"""

    def validate(*args, **kwargs):
        try:
            to_return = func(*args, **kwargs)
        except ValidationError as e:
            errors = []
            errors_list = json.loads(e.json())
            for error in errors_list:
                errors.append({"attribute": error["loc"][0], "msg": error["msg"]})
            return response(400, errors)
        except GenericError as e:
            return e.serialize_response()
        except MongoValidationError as e:
            return response(403, {"message": f"SOMETHING WENT WRONG {e}"})
        except OperationError as e:
            return response(406, {"message": "Tried to save duplicate unique keys"})
        except NotFoundError:
            return response(404, {"message": "Entity not found"})
        except Exception as e:
            raise e
        return to_return

    return validate
