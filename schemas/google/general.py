from marshmallow import Schema, fields, post_load

from datetime import datetime
from typing import List, Optional

from .doc import DocSchema
from ...dtos.google.general import (
    Auth,
    Common,
    DateInput,
    DateTimeInput,
    FormInput,
    General,
    StringInput,
    TimeInput,
    TimeZone
)
from ...dtos.google.literals import HostApp, Platform


class DateInputSchema(Schema):

    ms_since_epoch: str = fields.Str(data_key='msSinceEpoch')

    @post_load
    def make_date_input(self, data, **kwargs):
        return DateInput(**data)


class TimeInputSchema(Schema):

    hours: int = fields.Int()
    minutes: int = fields.Int()

    @post_load
    def make_time_input(self, data, **kwargs):
        return TimeInput(**data)


class DateTimeInputSchema(Schema):

    has_date: bool = fields.Bool(data_key='hasDate')
    has_time: bool = fields.Bool(data_key='hastime')
    ms_since_epoch: str = fields.Str(data_key='msSinceEpoch')

    @post_load
    def make_date_time_input(self, data, **kwargs):
        return DateTimeInput(**data)


class StringInputSchema(Schema):

    value: List[str] = fields.List(fields.Str())

    @post_load
    def make_general(self, data, **kwargs):
        return StringInput(**data)


class TimeZoneSchema(Schema):

    id: str = fields.Str()
    offset: int = fields.Int()

    @post_load
    def make_time_zone(self, data, **kwargs):
        return TimeZone(**data)


class FormInputSchema(Schema):
    stringInputs: Optional[StringInput] = fields.Nested(StringInputSchema, required=False)
    dateTimeInput: Optional[DateTimeInput] = fields.Nested(DateTimeInputSchema, required=False)
    dateInput: Optional[DateInput] = fields.Nested(DateInputSchema, required=False)
    timeInput: Optional[TimeInput] = fields. Nested(TimeInputSchema, required=False)

    @post_load
    def make_form_input(self, data, **kwargs):
        return FormInput(**data)


class CommonSchema(Schema):

    user_locale: str = fields.Str(data_key='userLocale')
    host_app: HostApp = fields.Str(data_key='hostApp')
    parameters: Optional[dict[str, str]] = fields.Dict()
    platform: Platform = fields.Str()
    time_zone: TimeZoneSchema = fields.Nested(TimeZoneSchema, data_key='timeZone')
    form_inputs: Optional[dict[str, FormInputSchema]] = fields.Dict(
        data_key='formInputs',
        keys=fields.Str(), 
        values=fields.Nested(FormInputSchema)
    )

    @post_load
    def make_common(self, data, **kwargs):
        return Common(**data)


class AuthSchema(Schema):

    system_id_token: str = fields.Str(data_key='systemIdToken')
    user_o_auth_token: str = fields.Str(data_key='userOAuthToken')
    user_email: str = fields.Str()
    user_id_token: str = fields.Str(data_key='userIdToken')
    email_verified: bool = fields.Bool()
    client_id: Optional[str] = fields.Str(required=False)
    expiry_timestamp: Optional[datetime] = fields.DateTime(required=False)
    issuer: Optional[str] = fields.Str(required=False)

    @post_load
    def make_auth(self, data, **kwargs):
        return Auth(**data)


class GeneralSchema(Schema):

    authorization_event_object: AuthSchema = fields.Nested(
        AuthSchema, data_key='authorizationEventObject')
    common_event_object: CommonSchema = fields.Nested(
        CommonSchema, data_key='commonEventObject')
    docs: DocSchema = fields.Nested(DocSchema)

    @post_load
    def make_general(self, data, **kwargs):
        return General(**data)
