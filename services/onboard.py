from dataclasses import dataclass
from os import getenv
from typing import List

from ..data.constants import ADD_USERS_URI, CARD_ID_REGISTRATION, CARD_ID_WELCOME, USER_REGISTRATION_FORM_URI
from ..dtos.google.action import Action
from ..dtos.google.button import Button
from ..dtos.google.card import Card
from ..dtos.google.color import Color
from ..dtos.google.decorated_text import DecoratedText
from ..dtos.google.footer import Footer
from ..dtos.google.header import Header
from ..dtos.google.icon import Icon, MaterialIcon
from ..dtos.google.input import SelectionInput, SelectionItem, TextInput, Validation
from ..dtos.google.literals import GoogleSource
from ..dtos.google.section import Section
from ..dtos.google.on_click import OnClick
from ..dtos.google.widget import Widget
from ..settings import BASE_URL
from ..utils.enums import AppsScriptFunction, BusinessCategory, MaterialIconName


@dataclass
class OnboardService:

    BASE_URL = getenv('BASE_URL')
    

    def _get_text_input(self, name: str, label:str, char_limit: int, required: bool = True, type: str = 'TEXT') -> TextInput:
        return TextInput(
            name=name,
            on_change_action=Action(required_widgets=[name]) if required else None,
            label=label,
            validation=Validation(character_limit=char_limit, input_type=type)
        )
    
    def _get_form_footer(self, text: str, altText: str, functionVal: str) -> Footer:
        return Footer(
            primary_button=Button(
                alt_text=altText,
                text=text,
                on_click=OnClick(action=Action(function=functionVal)),
                color=Color(red=0.20784, green=0.26667, blue=0.42745, alpha=1)
            )
        )

    def _get_form_widgets(self) -> List[Widget]:
        first_name_input: Widget = Widget(text_input=self._get_text_input('first_name', 'First Name', 15))
        last_name_input: Widget = Widget(text_input=self._get_text_input('last_name', 'Last Name', 15, False))
        org_section_text: Widget = Widget(decorated_text=DecoratedText(
            text='Organisation Info', start_icon=Icon(material_icon=MaterialIcon(name=MaterialIconName.CORPORATE.value))))
        org_name_input: Widget = Widget(text_input=self._get_text_input('organisation', 'Organisation', 20))
        org_category_input: Widget = Widget(
            selection_input=SelectionInput(
                label='Business Category',
                items=[SelectionItem(text=value.value, value=value.name) for value in BusinessCategory],
                name='category',
                on_change_action=Action(function='onChangeTextInput', required_widgets=['category'])
            )
        )
        website_url: Widget = Widget(text_input=self._get_text_input('website_url', 'Website URL', 120, False))

        return [
            first_name_input,
            last_name_input,
            Widget(divider={}),
            org_section_text,
            org_name_input,
            org_category_input,
            website_url,
        ]

    def get_registration_card(self, source: GoogleSource = 'ADDON') -> Card:
        '''Generates new user registration form card'''
        form_section: Section = Section(
            header='Tell us a little about yourself to get started',
            widgets=self._get_form_widgets()
        )
        functionVal: str = f'{self.BASE_URL}{ADD_USERS_URI}' if source == 'ADDON' else AppsScriptFunction.REGISTRATION_SUBMIT.value
        card: Card = Card(
            name=CARD_ID_REGISTRATION,
            header=Header('get stamping.'),
            display_style='REPLACE',
            sections=[form_section],
            fixed_footer=self._get_form_footer(text='CONTINUE', altText='Submit', functionVal=functionVal)
        )

        return card
    
    def get_welcome_screen(self, source: GoogleSource = 'ADDON') -> dict[str, object]:
        '''
        Gets Welcome card JSON object
        '''
        get_started_function: str = (
            f'{self.BASE_URL}{USER_REGISTRATION_FORM_URI}' 
            if source == 'ADDON' else AppsScriptFunction.REGISTRATION.value
        )
        # TODO: Replace with Card class
        card = {
            'name': CARD_ID_WELCOME,
            'header':{
                'subtitle': 'digital stamps made simple.',
                'imageUrl' : f'{BASE_URL}/static/img/logo.png',
                'imageType' : 'SQUARE',
                'title': 'veristamp.'
            },
            'sections': [
                {
                    'header': '<font color=\'#35446D\'><b>Why Veristamp?</b></font>',
                    'collapsible': False,
                    'uncollapsibleWidgetsCount': 1,
                    'widgets': [
                        {
                            'grid': {
                                'columnCount': 2,
                                'items': [
                                    {
                                        'image': {
                                            'imageUri': f'{BASE_URL}/static/img/welcome/stamp.png',
                                            'cropStyle': {
                                                'type': 'RECTANGLE_4_3'
                                            },
                                            'borderStyle': {
                                                'type': 'NO_BORDER'
                                            }
                                        },
                                        'title': None,
                                        'textAlignment': 'CENTER'
                                    },
                                    {
                                        'title': 'Create, edit, & manage unlimited stamps right from your Google Account',
                                        'textAlignment': 'START'
                                    },
                                    {
                                        'title': 'Apply stamps directly within Google docs',
                                        'textAlignment': 'END'
                                    },
                                    {
                                        'image': {
                                            'imageUri': f'{BASE_URL}/static/img/welcome/docs.png',
                                            'altText': 'Google Docs',
                                            'cropStyle': {
                                                'type': 'RECTANGLE_4_3'
                                            },
                                            'borderStyle': {
                                                'type': 'NO_BORDER'
                                            }
                                        },
                                        'title': None,
                                        'textAlignment': 'CENTER'
                                    },
                                    {
                                        'image': {
                                            'imageUri': f'{BASE_URL}/static/img/welcome/shield.png',
                                            'altText': 'Security Shield',
                                            'cropStyle': {
                                                'type': 'RECTANGLE_4_3'
                                            },
                                            'borderStyle': {
                                                'type': 'NO_BORDER'
                                            }
                                        },
                                        'title': None,
                                        'textAlignment': 'CENTER'
                                    },
                                    {
                                        'title': 'Enhance trust through stamps that can be verified via a simple lookup',
                                        'textAlignment': 'START'
                                    }
                                ]
                            }
                        }
                    ]
                },
                {
                    'header': None,
                    'collapsible': False,
                    'widgets': [
                        {
                            "textParagraph": {
                                "text": "Still got questions? <a href=\"https://www.google.com\">See More</a>.."
                            }
                        }
                    ]
                }
            ],
            'fixedFooter': {
                'primaryButton': {
                    'text': 'GET STARTED',
                    'icon': {
                        'materialIcon': {
                            'name': MaterialIconName.START.value
                        },
                        'altText': 'Sign up'
                    },
                    'color': {
                        "red": 0.20784,
                        "green": 0.26667,
                        "blue": 0.42745,
                        "alpha": 1
                    },
                    'onClick': {
                        "action": {
                            "function": get_started_function,
                            "loadIndicator": "SPINNER"
                        }
                    }
                }
            }
        }

        return card
