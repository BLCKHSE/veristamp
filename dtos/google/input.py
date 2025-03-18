from dataclasses import dataclass
from typing import List, Literal, Optional

from .action import Action
from .literals import InputType


@dataclass
class SelectionItem:

    bottom_text: Optional[str]
    selected: bool
    start_icon_uri: str
    text: str
    value: str


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

    external_dat_source: Optional[Action]
    label: str
    items: List[SelectionItem]
    multi_select_max_selected_items: int
    multi_select_min_query_length: int
    name: str
    on_change_action: Action
    platform_data_source: dict
    type: Literal['CHECK_BOX', 'RADIO_BUTTON', 'SWITCH', 'DROPDOWN', 'MULTI_SELECT']

@dataclass
class TextInput:

    auto_completion_action: Action
    label:str
    hint_text: Optional[str]
    initial_suggestions: Suggestions
    name: str
    on_change_action: Action
    placeholder_text: Optional[str]
    type: Literal['SINGLE_LINE', 'MULTIPLE_LINE']
    value: str
    validation: Validation
