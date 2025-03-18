from dataclasses import dataclass
from typing import List

from .icon import Icon


@dataclass
class OverflowMenuItem:
    startIcon: Icon
    text: str
    on_click: 'OnClick' # type: ignore
    disabled: bool = False


@dataclass
class OverflowMenu:
    items: List[OverflowMenuItem]
