from dataclasses import dataclass
from typing import Optional

from .button import Button
from .icon import Icon
from .switch_control import SwitchControl
from .on_click import OnClick


@dataclass
class DecoratedText:

    text: str
    wrap_text:bool = False
    bottom_label: Optional[str] = None
    on_click: Optional[OnClick] = None
    button: Optional[Button] = None
    switch_control: Optional[SwitchControl] = None
    start_icon: Icon = None
    top_label: str = None
    endIcon: Icon = None
