import functools
from pprint import pprint

from flask import jsonify, request
from marshmallow import ValidationError

from ..schemas.google.auth import Auth
from ..dtos.google.user import User


def authenticate(func):
    """Authenticates incoming request
    
    Keyword arguments:
    func -- function requiring quthentication
    Return: function wrpper
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        payload: dict = request.get_json()
        auth_event: object = payload.get('authorizationEventObject')
        try:
            _ = Auth().load(auth_event)
        except ValidationError as err:
            return jsonify({}), 403
        return func(*args, **kwargs)

    return wrapper
