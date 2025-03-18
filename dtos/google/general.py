from dataclasses import dataclass
from datetime import datetime
from typing import List, Literal, Optional, Union

from .doc import Doc
from .literals import HostApp, Platform


@dataclass
class DateInput:

    ms_since_epoch: str


@dataclass
class TimeInput:

    hours: int
    minutes: int


@dataclass
class DateTimeInput:

    has_date: bool
    has_time: bool
    ms_since_epoch: str


@dataclass
class StringInput:
    value: List[str]

@dataclass
class TimeZone:

    id: str
    offset: int


@dataclass
class FormInput:
    stringInputs: Optional[StringInput] = None
    dateTimeInput: Optional[DateTimeInput] = None
    dateInput: Optional[DateInput] = None
    timeInput: Optional[TimeInput] = None

    def __init__(self, **kwargs):
        if kwargs.get('stringInputs') != None:
            self.stringInputs = kwargs.get('stringInputs')
        elif kwargs.get('dateTimeInput') != None:
            self.dateTimeInput = kwargs.get('dateTimeInput')
        elif kwargs.get('dateInput') != None:
            self.dateInput = kwargs.get('dateInput')
        elif kwargs.get('timeInput') != None:
            self.timeInput = kwargs.get('timeInput')


@dataclass
class Common:

    user_locale: str
    host_app: HostApp
    platform: Platform
    time_zone: TimeZone
    form_inputs: dict[str, FormInput]


@dataclass
class Auth:

    system_id_token: str 
    user_o_auth_token: str
    user_email: str
    user_id_token: str
    email_verified: bool
    client_id: Optional[str] = None
    expiry_timestamp: Optional[datetime] = None
    issuer: Optional[str] = None

@dataclass
class General:

    authorization_event_object: Auth
    common_event_object: Common
    docs: Doc
