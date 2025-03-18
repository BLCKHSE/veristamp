from dataclasses import dataclass

from .button import Button


@dataclass
class Footer:
    primary_button: Button
    secondary_button: Button
