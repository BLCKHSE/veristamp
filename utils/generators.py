import random
import string

from ..settings import THEME_PRIMARY_COLOUR

class Generators:

    # TODO: Implement date based getAlphaNum

    @staticmethod
    def getAlphaNum(size: int) -> str:
        return ''.join(
            random.SystemRandom()
                .choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
            for _ in range(size)
        )
    
    @staticmethod
    def getSectionTitle(title: str) -> str:
        return f'<b><font color=\"{THEME_PRIMARY_COLOUR}\">{title}</font></b>'
    
    @staticmethod
    def getSectionSubtitle(subtitle: str) -> str:
        return f'<i>{subtitle}</i>'
