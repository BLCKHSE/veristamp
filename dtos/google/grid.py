from dataclasses import dataclass
from typing import List, Literal, Optional

from .border import BorderStyle
from .image import ImageComponent
from .on_click import OnClick


@dataclass
class GridItem:
    id: str
    image: ImageComponent
    layout: Literal['TEXT_BELOW', 'TEXT_ABOVE']
    title: str
    subtitle: Optional[str]


@dataclass
class Grid:

    column_count: int
    border_style: BorderStyle
    title: str
    items: List[GridItem]
    on_clicl: OnClick
