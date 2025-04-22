from dataclasses import dataclass
from typing import List, Literal, Optional

from .card import Card, ModifyCard
from .link import Link, LinkPreview, OpenLink


@dataclass
class ActionNavigation:

    action: Literal['CLOSE_DIALOG', 'CLOSE_DIALOG_AND_EXECUTE']


@dataclass
class ActionNotification:

    text: str


@dataclass
class Navigation:

    pop_to_root: Optional[bool] #pops all cards off except root card
    pop: Optional[bool] #pops one card off
    pop_to_card: Optional[bool]
    push_card: Optional[Card] #returns new card
    update_card: Optional[Card] #Updates the top card with a new card and preserves filled form fields values
    end_navigation: Optional[ActionNavigation]

    def __init__(self, **kwargs):
        if kwargs.get('pop_to_root', None) != None:
            self.pop_to_root = kwargs.get('pop_to_root')
        elif kwargs.get('pop', None) != None:
            self.pop = kwargs.get('pop')
        elif kwargs.get('pop_to_card', None) != None:
            self.pop_to_card= kwargs.get('pop_to_card')
        elif kwargs.get('push_card', None) != None:
            self.push_card = kwargs.get('push_card')
        elif kwargs.get('update_card', None) != None:
            self.update_card = kwargs.get('update_card')
        elif kwargs.get('end_navigation', None) != None:
            self.end_navigation = kwargs.get('end_navigation')


class ActionRenderAction:

    link: Optional[OpenLink]
    links: List[Link]
    link_preview: LinkPreview
    modify_operations: List[ModifyCard]
    navigations: List[Navigation]
    notification: ActionNotification

    def __init__(self, navigation: Navigation, notification_msg: str):
        self.notification = ActionNotification(notification_msg) if notification_msg != None else None
        self.navigations = [navigation]

@dataclass
class ActionRender():

    action: ActionRenderAction
    host_app_action: Optional[object]
    schema: Optional[str]

    def __init__(self, navigation: Navigation, notification_msg: str = None):
        self.action = ActionRenderAction(navigation, notification_msg)
