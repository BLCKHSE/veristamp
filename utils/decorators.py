import functools
import hashlib
import hmac
from os import getenv
from wsgiref.headers import Headers

from flask import jsonify, request
from marshmallow import ValidationError

from ..settings import PAYSTACK_IP_WHITELIST
from ..schemas.google.auth import Auth


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
            data = Auth().load(auth_event)
            kwargs['user_email'] = data['user_email']
        except ValidationError as err:
            return jsonify({}), 403
        return func(*args, **kwargs)

    return wrapper

def authenticate_paystack(func):
    """Authenticates incoming paystack webhooks
    
    Keyword arguments:
    func -- function requiring quthentication
    Return: function wrapper
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        headers: Headers = request.headers
        try:
            hash: str = hmac.new(
                getenv('PAYSTACK_API_SECRET').encode('utf-8'), 
                request.get_data(),
                hashlib.sha512
            ).hexdigest()
            if (
                    not hmac.compare_digest(hash, headers.get('X-Paystack-Signature'))
                    or headers.get('X-Forwarded-For') not in PAYSTACK_IP_WHITELIST
                ):
                raise Exception('Invalid signature')
        except Exception as err:
            return jsonify({}),403
        
        return func(*args, **kwargs)

    return wrapper
