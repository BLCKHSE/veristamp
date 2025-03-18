from dataclasses import dataclass

from .button import Button
from .literals import HorizontalAlignment


@dataclass
class CollapseControl:

    collapse_button: Button
    expand_button: Button
    horizontal_alignment: HorizontalAlignment
