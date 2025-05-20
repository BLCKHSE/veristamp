from distutils.util import strtobool
from os import getenv
from typing import List, Optional, Union

# FLASK
DEBUG: bool = bool(strtobool(getenv('DEBUG', 'false')))
SERVER_NAME: str = getenv(
    'SERVER_NAME', 'localhost:{0}'.format(getenv('PORT', '5000'))
)
TESTING: Union[bool, str] = getenv('TESTING', False)

CORS_ORIGINS: List[str] = [i.strip() for i in getenv('CORS_ORIGINS', '').split(",")]

# CACHE
CACHE_TYPE: Optional[str] = getenv('CACHE_TYPE')
CACHE_DEFAULT_TIMEOUT: int = int(getenv('CACHE_DEFAULT_TIMEOUT', 300))
CACHE_DIR: Optional[str] = getenv('CACHE_DIR')

# CLOUDINARY
CLOUDINARY_CLOUD_NAME: Optional[str] = getenv('CLOUDINARY_CLOUD_NAME') 
CLOUDINARY_API_KEY: Optional[str] = getenv('CLOUDINARY_API_KEY') 
CLOUDINARY_SECRET_KEY: Optional[str] = getenv('CLOUDINARY_SECRET_KEY') 
CLOUDINARY_URL: Optional[str] = getenv('CLOUDINARY_URL') 

# GOOGLE
GOOGLE_CLIENT_ID: Optional[str] = getenv('GOOGLE_CLIENT_ID')

# PAYSTACK
PAYSTACK_API_SECRET: Optional[str] = getenv('PAYSTACK_API_SECRET')
PAYSTACK_BASE_URL: Optional[str] = getenv('PAYSTACK_BASE_URL')
PAYSTACK_IP_WHITELIST: List[str] = getenv('PAYSTACK_IP_WHITELIST', '').split(',')
PAYSTACK_SUBSCRIPTION_URI: Optional[str] = getenv('PAYSTACK_SUBSCRIPTION_URL')

# SQLALCHEMY
SQLALCHEMY_DATABASE_URI: Optional[str] = getenv('DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS: bool = bool(strtobool(getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'True')))

# THEME
THEME_PRIMARY_COLOUR: str = getenv('PRIMARY_THEME_COLOUR', '#35446D')
THEME_PRIMARY_COLOUR_BLUE: float = float(getenv('PRIMARY_THEME_COLOUR_BLUE', '0.42745'))
THEME_PRIMARY_COLOUR_GREEN: float = float(getenv('PRIMARY_THEME_COLOUR_GREEN', '0.26667'))
THEME_PRIMARY_COLOUR_RED: float = float(getenv('PRIMARY_THEME_COLOUR_RED', '0.20784'))
THEME_SECONDARY_COLOUR: str = getenv('SECONDARY_THEME_COLOUR', '#E60012')
THEME_SECONDARY_COLOUR_BLUE: float = float(getenv('SECONDARY_THEME_COLOUR_BLUE', '0.07059'))
THEME_SECONDARY_COLOUR_GREEN: float = float(getenv('SECONDARY_THEME_COLOUR_GREEN', '0.90196'))
THEME_SECONDARY_COLOUR_RED: float = float(getenv('SECONDARY_THEME_COLOUR_RED', '0.90196'))

# API
BASE_URL: str = getenv('BASE_URL', 'http://127.0.0.1:5000')
