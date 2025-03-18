from dataclasses import dataclass
from typing import Optional

from .button import Button
from .icon import Icon
from .switch_control import SwitchControl
from .on_click import OnClick


@dataclass
class DecoratedText:

    start_icon: Icon
    top_label: str
    text: str
    wrap_text:bool
    bottom_label: Optional[str]
    on_click: Optional[OnClick]
    button: Optional[Button]
    switch_control: Optional[SwitchControl]
    endIcon: Icon
