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

    card_actions: List[CardAction]
    fixed_footer: Footer
    name: str
    header: Header
    peek_card_header: Header
    sections: List[Section]
    display_style: Literal['PEEK', 'REPLACE'] = 'REPLACE'
    section_divider_style: Literal['SOLID_DIVIDER', 'NO_DIVIDER'] = 'SOLID_DIVIDER'


@dataclass
class SelectionInputWidgetSuggestions:

    suggestions: List[SelectionInput]

@dataclass
class ModifyCard:
    update_widget: SelectionInputWidgetSuggestions
