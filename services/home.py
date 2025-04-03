from ..dtos.google.action import Action
from ..dtos.google.button import Button
from ..dtos.google.card import Card
from ..dtos.google.decorated_text import DecoratedText
from ..dtos.google.header import Header
from ..dtos.google.icon import Icon, MaterialIcon
from ..dtos.google.on_click import OnClick
from ..dtos.google.section import Section
from ..dtos.google.widget import Widget 
from ..models.user import User
from ..services.navigation import NavigationService
from ..settings import BASE_URL
from ..utils.enums import MaterialIconName, MenuItem
from ..utils.generators import Generators


class HomeService:
    '''Home screen service class'''

    CARD_ID_HOME = 'home.main'
    TEMPLATES_CARD_URI = '/api/template'

    def __init__(self):
        self._navigation_service = NavigationService()

    def _get_create_stamp_btn_wrapper(self)-> DecoratedText:
        '''Creates the 'Add Stamp' btn with a decoratedText wrapper to aid with positioning'''

        create_stamp_btn: Button = Button(
            alt_text='Create New Stamp',
            text=None,
            on_click=OnClick(Action(function=f'{BASE_URL}{self.TEMPLATES_CARD_URI}')),
            icon=Icon(alt_text='Add stamp', material_icon=MaterialIcon(name=MaterialIconName.ADD.value)),
            type='FILLED'
        )

        create_stamp_text: DecoratedText = DecoratedText(
            text=Generators.getSectionTitle('ADD STAMP'),
            bottom_label=Generators.getSectionSubtitle('create new stamp'),
            button=create_stamp_btn,
            start_icon=Icon(alt_text='Stamp icon', material_icon=MaterialIcon(name=MaterialIconName.STAMP.value)),
        )
        return create_stamp_text

    def get_home_card(self, user: User) -> Card:

        menu_section: Section = Section(
            header=None,
            widgets=[Widget(chip_list=self._navigation_service.get_menu(MenuItem.HOME))]
        )
        create_section: Section = Section(
            header=None,
            widgets=[Widget(decorated_text=self._get_create_stamp_btn_wrapper())]
        )
        # TODO: Add stamps grid

        card: Card = Card(
            name=self.CARD_ID_HOME,
            header=Header(f'Welcome, {user.first_name.upper()}'),
            sections=[menu_section, create_section]
        )
        return card
