from dataclasses import dataclass
from typing import Optional

from .action import Action
from .link import OpenLink
from .overflow_menu import OverflowMenu


@dataclass
class OnClick:

    action: Optional[Action]
    open_link: Optional[OpenLink]
    open_dynamic_link_action: Optional[Action]
    card: Optional['Card'] # type: ignore
    overflow_menu: Optional[OverflowMenu]
