from dataclasses import dataclass
from typing import List, Literal

from .literals import HorizontalAlignment, VerticalAlignment


@dataclass
class ColumnItem:

    horizontal_alignment: HorizontalAlignment
    horizontal_size_style: Literal['FILL_AVAILABLE_SPACE', 'FILL_MINIMUM_SPACE']
    vertical_alignment: VerticalAlignment
    widgets: List['Widget'] # type: ignore


@dataclass
class Columns:

    column_items: List[ColumnItem]
