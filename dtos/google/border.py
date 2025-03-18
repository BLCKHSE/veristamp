from dataclasses import dataclass
from typing import Literal, Optional

from .color import Color


@dataclass
class BorderStyle:

    corner_radius: Optional[int]
    stroke_color: Optional[Color]
    type: Literal['NO_BORDER', 'STRIKE']
