from dataclasses import dataclass
from typing import List, Literal, Optional

from .border import BorderStyle
from .literals import HorizontalAlignment
from .image import ImageComponent
from .on_click import OnClick


@dataclass
class GridItem:
    id: str
    title: str
    image: Optional[ImageComponent] = None
    layout: Literal['TEXT_BELOW', 'TEXT_ABOVE'] = 'TEXT_BELOW'
    subtitle: Optional[str] = None
    text_alignment: HorizontalAlignment = 'CENTER'


@dataclass
class Grid:

    column_count: int
    items: List[GridItem]
    on_click: OnClick
    border_style: BorderStyle = BorderStyle(1)
    title: Optional[str] = None
