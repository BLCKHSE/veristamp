from dataclasses import dataclass
from typing import List

from .collapse_control import CollapseControl
from .widget import Widget


@dataclass
class Section:

    header: str
    widgets: List[Widget]
    collapsible: bool = False
    uncollapsible_widget_count: int = 1
    collapse_control: CollapseControl = None
