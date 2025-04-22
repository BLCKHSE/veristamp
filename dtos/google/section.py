from dataclasses import dataclass
from typing import List, Optional

from .collapse_control import CollapseControl
from .widget import Widget


@dataclass
class Section:

    widgets: List[Widget]
    collapsible: bool = False
    header: Optional[str] = None
    uncollapsible_widget_count: int = 1
    collapse_control: CollapseControl = None
