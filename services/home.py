from ..dtos.google.card import Card
from ..dtos.google.header import Header
from ..dtos.google.image import Image
from ..dtos.google.section import Section
from ..dtos.google.widget import Widget
from ..models.user import User
from ..settings import BASE_URL


class HomeService:
    '''Home screen service class'''

    CARD_ID = 'home.main'

    def get_home_card(self, user: User):

        test_widget: Widget = Widget(image=Image('logo image', f'{BASE_URL}/static/img/logo+txt.png'))

        test_section: Section = Section(
            header='<font color=\'#35446D\'>Placeholder</font>',
            widgets=[test_widget]
        )

        card: Card = Card(
            name=self.CARD_ID,
            header=Header(f'Welcome, {user.first_name.upper()}'),
            sections=[test_section]
        )
        return card
