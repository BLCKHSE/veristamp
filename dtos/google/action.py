from dataclasses import dataclass
from typing import List, Literal, Optional

@dataclass
class Action:
    
    all_widgets_are_required: Optional[bool]
    function: Optional[str]
    parameters: List[dict]
    load_indicator: Literal['SPINNER', 'NONE']
    persist_values: bool = False
    required_widgets: List[str] = None
    interaction: Literal['INTERACTION_UNSPECIFIED', 'OPEN_DIALOG'] = 'INTERACTION_UNSPECIFIED'
