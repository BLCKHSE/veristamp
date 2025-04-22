from typing import List, Literal, Optional

from marshmallow import Schema, fields, post_dump, post_load

from .action import ActionSchema
from ...dtos.google.literals import InputType
from ...dtos.google.input import DateTimePicker, SelectionInput, SuggestionItem, Suggestions, TextInput, Validation


class SelectionItemSchema(Schema):

    bottom_text: Optional[str] = fields.Str()
    selected: bool = fields.Bool()
    start_icon_uri: str = fields.Str(data_key='startIconUri')
    text: str = fields.Str()
    value: str = fields.Str()

    @post_load
    def make_selection_item(self, data, **kwargs):
        return SelectionInput(**data)


class SuggestionItemSchema(Schema):

    text: str = fields.Str()

    @post_load
    def make_suggestion_input(self, data, **kwargs):
        return SuggestionItem(**data)


class SuggestionsSchema(Schema):

    items: List[SuggestionItemSchema] = fields.Nested(SuggestionItemSchema)

    @post_load
    def make_suggestions(self, data, **kwargs):
        return Suggestions(**data)


class ValidationSchema(Schema):
    character_limit: int = fields.Int(data_key='characterLimit')
    input_type: InputType = fields.Str(data_key='inputType')

    @post_load
    def make_validation(self, data, **kwargs):
        return Validation(**data)


class DateTimePickerSchema(Schema):

    label: str = fields.Str()
    name : str = fields.Str()
    on_change_action: Optional[ActionSchema] = fields.Nested(ActionSchema, data_key='onChangeAction')
    timezone_offset_date: Optional[int] = fields.Int(data_key='timezoneOffsetDate')
    type: Literal['DATE_AND_TIME', 'DATE_ONLY', 'TIME_ONLY'] = fields.Str()
    value_ms_epoch: int = fields.Int()

    @post_load
    def make_dat_time_picker(self, data, **kwargs):
        return DateTimePicker(**data)


class SelectionInputSchema(Schema):

    external_data_source: Optional[ActionSchema] = fields.Nested(ActionSchema, data_key='externalDataSource')
    label: str = fields.Str()
    items: List[SelectionItemSchema] = fields.List(fields.Nested(SelectionItemSchema))
    multi_select_max_selected_items: int = fields.Int(data_key='multiSelectMaxSelectedItems')
    multi_select_min_query_length: int = fields.Int(data_key='multiSelectMinQueryLength')
    name: str = fields.Str()
    on_change_action: ActionSchema = fields.Nested(ActionSchema , data_key='onChangeAction')
    platform_data_source: dict = fields.Dict(data_key='platformDataSource')
    type: Literal['CHECK_BOX', 'RADIO_BUTTON', 'SWITCH', 'DROPDOWN', 'MULTI_SELECT'] = fields.Str()

    @post_load
    def make_selection_input(self, data, **kwargs):
        return SelectionInput(**data)


class TextInputSchema(Schema):

    auto_completion_action: ActionSchema = fields.Nested(ActionSchema , data_key='autoCompletionAction')
    label:str = fields.Str()
    hint_text: Optional[str] = fields.Str(data_key='hintText')
    initial_suggestions: SuggestionsSchema = fields.Nested(SuggestionsSchema)
    name: str = fields.Str()
    on_change_action: ActionSchema = fields.Nested(ActionSchema, data_key='onChangeAction')
    placeholder_text: Optional[str] = fields.Str(data_key='placeholderText')
    type: Literal['SINGLE_LINE', 'MULTIPLE_LINE'] = fields.Str()
    value: str = fields.Str()
    validation: ValidationSchema = fields.Nested(ValidationSchema)

    @post_load
    def make_text_input(self, data, **_):
        return TextInput(**data)
    
    @post_dump
    def remove_empty_values(self, data, **_):
        return {
            key: value for key, value in data.items()
            if value is not None
        }
