# * Import Python Modules
import json
from functools import wraps
from flask import request
from pydantic import ValidationError

# * Import User Defined Function
from utils.response_utils import response


def pydantic_validation(model_name):
    """
    A decorator function that performs Pydantic validation on the incoming request data
    and returns an error response if validation fails.

    Args:
        model_name (pydantic.BaseModel): The Pydantic model to use for validation.

    Returns:
        function: The decorated function.
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                # Parse request data and validate it using the specified Pydantic model
                if request.method == "GET":
                    data = request.args.to_dict()
                    pass
                elif request.method == "POST" or request.method == "PUT":
                    data = json.loads(request.data)
                model_name(**data)
                return f(*args, **kwargs)
            except ValidationError as e:
                # If validation fails, create an error response with the error messages
                errors = []
                errors_list = json.loads(e.json())
                for error in errors_list:
                    errors.append({"attribute": error["loc"][0], "msg": error["msg"]})
                response_body = {
                    "errors": errors,
                    "status": False,
                    "message": "Validation Error",
                }
                return response(400, response_body)

        return decorated_function

    return decorator
