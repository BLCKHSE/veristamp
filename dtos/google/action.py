from dataclasses import dataclass
from typing import List, Literal, Optional


@dataclass
class ActionParameter:

    key: str
    value: str


@dataclass
class Action:
    
    function: Optional[str]
    all_widgets_are_required: Optional[bool] = False
    interaction: Literal['INTERACTION_UNSPECIFIED', 'OPEN_DIALOG'] = 'INTERACTION_UNSPECIFIED'
    load_indicator: Literal['SPINNER', 'NONE'] = 'SPINNER'
    parameters: List[ActionParameter] = None
    persist_values: bool = False
    required_widgets: List[str] = None
