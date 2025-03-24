from dataclasses import dataclass
from typing import List, Literal

from .on_click import OnClick
from .footer import Footer
from .header import Header
from .input import SelectionInput
from .section import Section


@dataclass
class CardAction:
    actionLabel: str
    on_click: OnClick

@dataclass
class Card:

    name: str
    header: Header
    sections: List[Section]
    card_actions: List[CardAction] = None
    display_style: Literal['PEEK', 'REPLACE'] = 'REPLACE'
    fixed_footer: Footer = None
    peek_card_header: Header = None
    section_divider_style: Literal['SOLID_DIVIDER', 'NO_DIVIDER'] = 'SOLID_DIVIDER'


@dataclass
class SelectionInputWidgetSuggestions:

    suggestions: List[SelectionInput]

@dataclass
class ModifyCard:
    update_widget: SelectionInputWidgetSuggestions
