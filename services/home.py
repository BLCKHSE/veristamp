from ..dtos.google.card import Card
from ..dtos.google.chips import ChipList
from ..dtos.google.header import Header
from ..dtos.google.image import Image
from ..dtos.google.section import Section
from ..dtos.google.widget import Widget
from ..models.user import User
from ..services.navigation import NavigationService
from ..settings import BASE_URL
from ..utils.enums import MenuItem


class HomeService:
    '''Home screen service class'''

    CARD_ID_HOME = 'home.main'

    def __init__(self):
        self._navigation_service = NavigationService()

    def get_home_card(self, user: User):

        test_widget: Widget = Widget(image=Image('logo image', f'{BASE_URL}/static/img/logo+txt.png'))
        menu: Widget = Widget(chip_list=self._navigation_service.get_menu(MenuItem.HOME))

        test_section: Section = Section(
            header=None,
            widgets=[menu, test_widget]
        )

        card: Card = Card(
            name=self.CARD_ID_HOME,
            header=Header(f'Welcome, {user.first_name.upper()}'),
            sections=[test_section]
        )
        return card
