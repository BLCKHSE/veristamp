from dataclasses import dataclass
from typing import Optional

from .literals import ImageType, KnownIcon


@dataclass
class MaterialIcon:
    name: str
    weight: int
    grade: int
    fill: bool = False


@dataclass
class Icon:
    altText: Optional[str]
    icon_url: Optional[str]
    image_type: ImageType
    known_icon: Optional[KnownIcon]
    material_icon: Optional[MaterialIcon]
