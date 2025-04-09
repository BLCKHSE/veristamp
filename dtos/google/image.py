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

    aspect_ratio: Optional[float] = None
    type: Literal['SQUARE', 'CIRCLE', 'RECTANGLE_CUSTOM', 'RECTANGLE_4_3'] = 'SQUARE'

@dataclass
class ImageComponent:

    image_uri: str
    alt_text: Optional[str] = None
    border_style: BorderStyle = BorderStyle(1)
    crop_style: ImageCropStyle = ImageCropStyle()
