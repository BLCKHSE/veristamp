from dataclasses import dataclass
from os import getenv
from typing import List, Literal, Optional

from .color import Color
from .icon import Icon
from .on_click import OnClick


@dataclass
class Button:

    alt_text: Optional[str]
    text: Optional[str]
    on_click: Optional[OnClick]
    color: Optional[Color]  = Color()
    icon: Optional[Icon] = None
    type: Literal['OUTLINED', 'FILLED', 'FILLED_TONAL', 'BORDERLESS'] = 'OUTLINED'
    disabled: Optional[bool] = False


@dataclass
class ButtonList:

    buttons: List[Button]
