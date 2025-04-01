from typing import List, Optional

from ..dtos.google.action import Action
from ..dtos.google.chips import Chip, ChipList
from ..dtos.google.icon import Icon, MaterialIcon
from ..dtos.google.on_click import OnClick
from ..settings import BASE_URL
from ..utils.enums import MenuItem


MENU_ITEMS: List[dict] = [
    {
        'label': MenuItem.HOME,
        'action': '/api/home',
        'material_icon': 'home'
    },
    {
        'label': MenuItem.DASHBOARD,
        'action': '/api/dashboard',
        'material_icon': 'dashboard_2'
    },
    {
        'label': MenuItem.USERS,
        'action': '/api/admin/users',
        'material_icon': 'group'
    }
]

class NavigationService:

    def _get_menu_chip(self, action: str, icon: str, label: Optional[str])-> Chip:
        on_click: OnClick = OnClick(action=Action(function=f'{BASE_URL}{action}'))
        icon: Icon = Icon(alt_text=f'{label} menu icon', material_icon=MaterialIcon(name=icon))
        chip: Chip = Chip(
            on_click=on_click,
            icon=icon,
            alt_text=f'Opens {label} page',
            label=(label if label != MenuItem.HOME.name else None)
        )
        return chip

    def get_menu(self, active_page: MenuItem = MenuItem.HOME) -> ChipList:
        chips: List[Chip] = []
        for item in MENU_ITEMS:
            chip: Chip = self._get_menu_chip(
                action=item.get('action'),
                icon=item.get('material_icon'),
                label=item.get('label').name
            )
            chip.disabled = True if active_page == item.get('label') else chip.disabled
            chips.append(chip)

        chips_list: ChipList = ChipList(chips=chips, layout='HORIZONTAL_SCROLLABLE')
        return chips_list
