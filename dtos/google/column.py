from dataclasses import dataclass
from typing import List, Literal, Optional

from ...dtos.google.button import ButtonList
from ...dtos.google.chips import ChipList
from ...dtos.google.decorated_text import DecoratedText
from ...dtos.google.image import Image
from ...dtos.google.input import SelectionInput, TextInput
from ...dtos.google.paragraph import Paragraph

from .literals import HorizontalAlignment, VerticalAlignment


@dataclass
class Widget:

    button_list: Optional[ButtonList] = None
    chip_list: Optional[ChipList] = None
    decorated_text: Optional[DecoratedText] = None
    selection_input: Optional[SelectionInput] = None
    text_input: Optional[TextInput] = None
    text_paragraph: Optional[Paragraph] = None
    image: Optional[Image] = None


@dataclass
class ColumnItem:

    widgets: List[Widget]
    horizontal_alignment: HorizontalAlignment = 'CENTER'
    horizontal_size_style: Literal['FILL_AVAILABLE_SPACE', 'FILL_MINIMUM_SPACE'] = 'FILL_AVAILABLE_SPACE'
    vertical_alignment: VerticalAlignment = 'CENTER'


@dataclass
class Columns:

    column_items: List[ColumnItem]
