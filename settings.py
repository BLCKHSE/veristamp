from distutils.util import strtobool
from os import getenv
from typing import List

# FLASK
DEBUG: bool = bool(strtobool(getenv('DEBUG', 'false')))
SERVER_NAME: str = getenv(
    'SERVER_NAME', 'localhost:{0}'.format(getenv('PORT', '5000'))
)
TESTING: bool = getenv('TESTING', False)

CORS_ORIGINS: List[str] = [i.strip() for i in getenv('CORS_ORIGINS').split(",")]

# GOOGLE
GOOGLE_CLIENT_ID: str = getenv('GOOGLE_CLIENT_ID')

# PAYSTACK
PAYSTACK_API_SECRET: str = getenv('PAYSTACK_API_SECRET')
PAYSTACK_BASE_URL: str = getenv('PAYSTACK_BASE_URL')
PAYSTACK_IP_WHITELIST: List[str] = getenv('PAYSTACK_IP_WHITELIST').split(',')
PAYSTACK_SUBSCRIPTION_URI: str = getenv('PAYSTACK_SUBSCRIPTION_URL')

# SQLALCHEMY
SQLALCHEMY_DATABASE_URI: str = getenv('DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS: bool = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

# API
BASE_URL: str = getenv('BASE_URL', 'http://127.0.0.1:5000')
