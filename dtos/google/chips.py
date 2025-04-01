from dataclasses import dataclass
from typing import List, Literal, Optional

from .icon import Icon
from .on_click import OnClick


@dataclass
class Chip:

    on_click: OnClick
    icon: Optional[Icon] = None
    alt_text: Optional[str] = None
    disabled: bool = False
    label: Optional[str] = None


@dataclass
class ChipList:

    chips: List[Chip]
    layout: Literal['WRAPPED', 'HORIZONTAL_SCROLLABLE'] = 'WRAPPED'
