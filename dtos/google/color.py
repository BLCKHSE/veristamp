from dataclasses import dataclass
from os import getenv


@dataclass
class Color:

    red: float
    green: float
    blue: float
    alpha: int = 1

    def __init__(self, **kwargs):
        self.red = kwargs.get('red') if kwargs.get('red') != None else getenv('PRIMARY_THEME_COLOUR_RED')
        self.blue = kwargs.get('blue') if kwargs.get('blue') != None else getenv('PRIMARY_THEME_COLOUR_BLUE')
        self.green = kwargs.get('green') if kwargs.get('green') != None else  getenv('PRIMARY_THEME_COLOUR_GREEN')
