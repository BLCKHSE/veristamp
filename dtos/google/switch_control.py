from dataclasses import dataclass

from .action import Action
from .literals import ControlType


@dataclass
class SwitchControl:

    control_type: ControlType
    name: str
    value: str
    selected: bool
    onChangeAction: Action
