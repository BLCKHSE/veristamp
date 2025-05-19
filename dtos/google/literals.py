from typing import Literal


ControlType = Literal['SWITCH', 'CHECKBOX']

DisplayStyle = Literal['REPLACE', 'PEEK']

HorizontalAlignment = Literal['START', 'CENTER', 'END']

HostApp = Literal['GMAIL', 'CALENDAR', 'DRIVE', 'DOCS', 'SHEETS', 'SLIDES']

ImageType =  Literal['SQUARE', 'CIRCLE']

InputType = Literal['TEXT', 'INTEGER', 'FLOAT', 'EMAIL', 'EMOJI_PICKER']

KnownIcon = Literal[
    'AIRPLANE', 'BOOKMARK', 'BUS', 'CAR', 'CLOCK', 'CONFIRMATION_NUMBER_ICON', 'DESCRIPTION', 'DOLLAR',
    'EMAIL', 'EVENT_SEAT', 'FLIGHT_ARRIVAL', 'FLIGHT_DEPARTURE', 'HOTEL', 'HOTEL_ROOM_TYPE', 'INVITE', 
    'MAP_PIN', 'MEMBERSHIP', 'MULTIPLE_PEOPLE', 'PERSON', 'PHONE', 'RESTAURANT_ICON', 'SHOPPING_CART',
    'STAR', 'STORE', 'TICKET', 'TRAIN', 'VIDEO_CAMERA', 'VIDEO_PLAY',
]

Platform = Literal['WEB', 'IOS', 'ANDROID']

GoogleSource = Literal['APPS_SCRIPT', 'ADDON']

VerticalAlignment = Literal['CENTER', 'TOP', 'BOTTOM']
