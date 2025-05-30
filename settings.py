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

# CACHE
CACHE_TYPE: str = getenv('CACHE_TYPE')
CACHE_DEFAULT_TIMEOUT: int = int(getenv('CACHE_DEFAULT_TIMEOUT'))
CACHE_DIR: str = getenv('CACHE_DIR')

# CLOUDINARY
CLOUDINARY_CLOUD_NAME: str = getenv('CLOUDINARY_CLOUD_NAME') 
CLOUDINARY_API_KEY: str = getenv('CLOUDINARY_API_KEY') 
CLOUDINARY_SECRET_KEY: str = getenv('CLOUDINARY_SECRET_KEY') 
CLOUDINARY_URL: str = getenv('CLOUDINARY_URL') 

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

# THEME
THEME_PRIMARY_COLOUR: str = getenv('PRIMARY_THEME_COLOUR')
THEME_PRIMARY_COLOUR_BLUE: float = getenv('PRIMARY_THEME_COLOUR_BLUE')
THEME_PRIMARY_COLOUR_GREEN: float = getenv('PRIMARY_THEME_COLOUR_GREEN')
THEME_PRIMARY_COLOUR_RED: float = getenv('PRIMARY_THEME_COLOUR_RED')
THEME_SECONDARY_COLOUR: str = getenv('SECONDARY_THEME_COLOUR')
THEME_SECONDARY_COLOUR_BLUE: float = getenv('SECONDARY_THEME_COLOUR_BLUE')
THEME_SECONDARY_COLOUR_GREEN: float = getenv('SECONDARY_THEME_COLOUR_GREEN')
THEME_SECONDARY_COLOUR_RED: float = getenv('SECONDARY_THEME_COLOUR_RED')

# API
BASE_URL: str = getenv('BASE_URL', 'http://127.0.0.1:5000')
