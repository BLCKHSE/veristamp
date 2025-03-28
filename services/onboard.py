from dataclasses import dataclass
from os import getenv

from ..dtos.google.header import Header
from ..utils.enums import BusinessCategory


@dataclass
class OnboardService:

    BASE_URL = getenv('BASE_URL')
    CARD_ID_REGISTRATION = 'get-started.registration'
    CARD_ID_WELCOME = 'get-started.welcome'

    def get_registration_card(self) -> dict[str, object]:
        card = {
            'name': self.CARD_ID_REGISTRATION,
            'header': Header('get stamping.'),
            'displayStyle': 'REPLACE',
            'sections': [
                {
                    "header": "Tell us a little about yourself to get started",
                    "collapsible": False,
                    "uncollapsibleWidgetsCount": 1,
                    "widgets": [
                        {
                            "textInput": {
                                "name": "first_name",
                                "label": "First Name",
                                "validation": {
                                    "inputType": "TEXT",
                                    "characterLimit": 15
                                },
                                "onChangeAction": {
                                    "function": "onChangeTextInput",
                                    "requiredWidgets": [
                                        "first_name"
                                    ]
                                }
                            }
                        },
                        {
                            "textInput": {
                                "name": "last_name",
                                "label": "Last Name",
                                "validation": {
                                    "inputType": "TEXT",
                                    "characterLimit": 15
                                }
                            }
                        },
                        {
                            "divider": {}
                        },
                        {
                            "textParagraph": {
                                "text": "Organisation Info",
                                "maxLines": 3
                            }
                        },
                        {
                            "textInput": {
                                "name": "organisation",
                                "label": "Organisation",
                                "validation": {
                                    "inputType": "TEXT",
                                    "characterLimit": 20
                                },
                                "onChangeAction": {
                                    "function": "onChangeTextInput",
                                    "requiredWidgets": ["organisation"]
                                }
                            }
                        },
                        {
                        "selectionInput": {
                            "name": "category",
                            "label": "Business Category",
                            "type": "DROPDOWN",
                            "items": [
                                {"text": value.value , "value": value.name, "selected": False} for value in BusinessCategory
                            ],
                            "onChangeAction": {
                                "function": "onChangeTextInput",
                                "requiredWidgets": ["category"]
                            }
                        }
                        },
                        {
                        "textInput": {
                            "name": "website_url",
                            "label": "Website URL",
                            "validation": {
                            "inputType": "TEXT"
                            }
                        }
                        }
                    ]
                }
            ],
            "fixedFooter": {
                "primaryButton": {
                    "text": "CONTINUE",
                    "color": {
                        "red": 0.20784,
                        "green": 0.26667,
                        "blue": 0.42745,
                        "alpha": 1
                    },
                    "onClick": {
                        "action": {
                            "function": f"{self.BASE_URL}/api/users",
                            "loadIndicator": "SPINNER"
                        }
                    }
                }
            }

        } 

        return card
    
    def get_welcome_screen(self) -> dict[str, object]:
        '''
        Gets Welcome card JSON object
        '''
        card = {
            'name': self.CARD_ID_WELCOME,
            'header': Header('digital stamps made simple.'),
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
                                            'imageUri': f'{getenv("BASE_URL")}/static/img/welcome/stamp.png',
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
                                            'imageUri': f'{getenv("BASE_URL")}/static/img/welcome/docs.png',
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
                                            'imageUri': f'{getenv("BASE_URL")}/static/img/welcome/shield.png',
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
                            "buttonList": {
                                "buttons": [
                                    {
                                        "text": "GET STARTED",
                                        "icon": {
                                            "materialIcon": {
                                                "name": "start"
                                            },
                                            "altText": "Sign up"
                                        },
                                        "color": {
                                            "red": 0.20784,
                                            "green": 0.26667,
                                            "blue": 0.42745,
                                            "alpha": 1
                                        },
                                        "type": "FILLED",
                                        "onClick": {
                                            "card": self.get_registration_card()
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "textParagraph": {
                                "text": "Still got questions? <a href=\"https://www.google.com\">See More</a>.."
                            }
                        }
                    ]
                }
            ]
        }

        return card
