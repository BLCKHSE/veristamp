from dataclasses import dataclass, field
from typing import Dict, Optional

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

    button_list: Optional[ButtonList] = None
    columns: Optional[Columns] = None
    date_time_picker: Optional[DateTimePicker] = None
    decorated_text: Optional[DecoratedText] = None
    grid: Optional[Grid] = None
    horizontal_alignment: HorizontalAlignment = None
    selection_input: Optional[SelectionInput] = None
    text_input: TextInput = None
    text_paragraph: Optional[Paragraph] = None
    image: Optional[Image] = None
    divider: Dict[str, object] = None
