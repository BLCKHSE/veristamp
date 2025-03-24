
from dataclasses import dataclass
from os import getenv
from typing import Optional

from .literals import ImageType


@dataclass
class Header:

    title: str
    subtitle: Optional[str]
    image_url: Optional[str]
    image_type: ImageType

    def __init__(
        self, 
        sub_title:str = None,
        image_url: Optional[str] = f"{getenv('BASE_URL')}/static/img/logo.png",
        image_type: Optional[ImageType] = 'CIRCLE',
        title: str = 'veristamp.'
    ):
        self.title = title
        self.image_type = image_type
        self.image_url = image_url
        self.subtitle = sub_title
