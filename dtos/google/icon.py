from dataclasses import dataclass
from typing import Optional

from .literals import ImageType, KnownIcon


@dataclass
class MaterialIcon:
    name: str
    weight: int = None
    grade: int = None
    fill: bool = False


@dataclass
class Icon:
    altText: Optional[str] = None
    icon_url: Optional[str] = None
    image_type: ImageType = 'SQUARE'
    known_icon: Optional[KnownIcon] = None
    material_icon: Optional[MaterialIcon] = None
