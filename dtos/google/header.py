
from dataclasses import dataclass
from typing import Optional

from .literals import ImageType


@dataclass
class Header:

    title: str
    subtitle: Optional[str]
    image_url: Optional[str]
    image_type: ImageType
