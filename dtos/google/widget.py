from dataclasses import dataclass
from typing import Optional

from .button import ButtonList
from .column import Columns
from .decorated_text import DecoratedText
from .grid import Grid
from .image import Image
from .input import DateTimePicker, SelectionInput, TextInput
from .literals import HorizontalAlignment
from .paragraph import Paragraph

@dataclass
class Widget:

    button_list: Optional[ButtonList]
    columns: Optional[Columns]
    date_time_picker: Optional[DateTimePicker]
    decorated_text: Optional[DecoratedText]
    grid: Optional[Grid]
    horizontal_alignment: HorizontalAlignment
    selection_input: Optional[SelectionInput]
    text_input: TextInput
    text_paragraph: Optional[Paragraph]
    image: Optional[Image]
    divider: dict[str, object]
