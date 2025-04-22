from dataclasses import dataclass
from typing import List, Literal, Optional

from .action import Action
from .literals import InputType


@dataclass
class SelectionItem:

    text: str
    value: str
    bottom_text: Optional[str] = None
    selected: bool = False
    start_icon_uri: Optional[str] = None


@dataclass
class SuggestionItem:

    text: str


@dataclass
class Suggestions:

    items: List[SuggestionItem]


@dataclass
class Validation:
    character_limit: int
    input_type: InputType


@dataclass
class DateTimePicker:

    label: str
    name : str
    on_change_action: Optional[Action]
    timezone_offset_date: Optional[int]
    type: Literal['DATE_AND_TIME', 'DATE_ONLY', 'TIME_ONLY']
    value_ms_epoch: int


@dataclass
class SelectionInput:

    label: str
    items: List[SelectionItem]
    name: str
    external_data_source: Optional[Action] = None
    multi_select_max_selected_items: Optional[int] = None
    multi_select_min_query_length: Optional[int] = None
    on_change_action: Optional[Action] = None
    platform_data_source: Optional[dict] = None
    type: Literal['CHECK_BOX', 'RADIO_BUTTON', 'SWITCH', 'DROPDOWN', 'MULTI_SELECT'] = 'DROPDOWN'


@dataclass
class TextInput:

    name: str
    on_change_action: Action
    auto_completion_action: Optional[Action] = None
    hint_text: Optional[str] = None # Required if label is unspecified.
    initial_suggestions: Optional[Suggestions] = None
    label:Optional[str] = None
    type: Literal['SINGLE_LINE', 'MULTIPLE_LINE'] = 'SINGLE_LINE'
    placeholder_text: Optional[str] = None
    validation: Optional[Validation] = None
    value: Optional[str] = None
