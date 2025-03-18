from dataclasses import dataclass
from typing import List

from .collapse_control import CollapseControl
from .widget import Widget


@dataclass
class Section:

    header: str
    collapsible: bool
    uncollapsible_widegt_count: int
    collapse_control: CollapseControl
    widgets: List[Widget]
