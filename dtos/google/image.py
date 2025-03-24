from dataclasses import dataclass
from typing import Literal, Optional

from .border import BorderStyle
from .on_click import OnClick


@dataclass
class Image:

    alt_text: Optional[str]
    image_url: str
    on_click: Optional[OnClick] = None


@dataclass
class ImageCropStyle:

    aspect_ratio: Optional[float]
    type: Literal['SQUARE', 'CIRCLE', 'RECTANGLE_CUSTOM', 'RECTANGLE_4_3']

@dataclass
class ImageComponent:

    border_style: BorderStyle
    crop_style: ImageCropStyle
    alt_text: Optional[str]
    image_uri: str
