from dataclasses import dataclass
from typing import List, Literal, Optional

from .color import Color
from .icon import Icon
from .on_click import OnClick


@dataclass
class Button:

    alt_text: Optional[str]
    color: Optional[Color]
    icon: object
    text: str
    type: Literal['OUTLINED', 'FILLED', 'FILLED_TONAL', 'BORDERLESS']
    icon: Optional[Icon]
    on_click: Optional[OnClick]
    disabled: Optional[bool] = False


@dataclass
class ButtonList:

    buttons: List[Button]
