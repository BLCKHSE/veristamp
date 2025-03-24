from typing import List, Optional
from marshmallow import Schema, fields, post_load, validate

from .color import ColorSchema
from .icon import IconSchema
from .on_click import OnClickSchema
from ...dtos.google.button import Button, ButtonList


class ButtonSchema(Schema):

    alt_text: Optional[str] = fields.Str(data_key='altText')
    color: Optional[ColorSchema] = fields.Nested(ColorSchema)
    icon: object = fields.Dict()
    text: str = fields.Str()
    type: str = fields.Str(
        validate=[validate.OneOf(choices= ['OUTLINED', 'FILLED', 'FILLED_TONAL', 'BORDERLESS'])])
    icon: Optional[IconSchema] = fields.Nested(IconSchema)
    on_click: Optional[OnClickSchema] = fields.Nested(OnClickSchema, data_key='onClick')
    disabled: Optional[bool] = fields.Bool(dump_default=False)

    @post_load
    def make_button(self, data, **kwargs):
        return Button(**data)


class ButtonListSchema(Schema):

    buttons: List[ButtonSchema] = fields.List(fields.Nested(ButtonSchema))

    @post_load
    def make_button_list(self, data, **kwargs):
        return ButtonList(**data)
