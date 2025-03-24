from dataclasses import dataclass
from typing import Optional

from .action import Action
from .link import OpenLink
from .overflow_menu import OverflowMenu


@dataclass
class OnClick:

    action: Optional[Action] = None
    open_link: Optional[OpenLink] = None
    open_dynamic_link_action: Optional[Action] = None
    card: Optional['Card'] = None # type: ignore
    overflow_menu: Optional[OverflowMenu] = None
