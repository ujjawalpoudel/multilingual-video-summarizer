# * Import Python Module
from flask import make_response


def response(status_code, body):
    """Build a standard JSON response

    Args:
        code: int: HTTP status code
        body: AnyOf [JSON serializable string, dict]: Body to serialize
    """
    response_body = {
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": body,
        "isBase64Encoded": False,
    }
    return make_response(response_body, status_code)
