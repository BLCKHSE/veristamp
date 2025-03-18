from typing import Optional
from marshmallow import Schema, fields

from .button import ButtonSchema
from .icon import IconSchema
from .on_click import OnClickSchema
from .switch_control import SwitchControlSchema


class DecoratedTextSchema(Schema):

    start_icon: IconSchema = fields.Nested(IconSchema )
    top_label: str = fields.Str(data_key='topLabel')
    text: str = fields.Str()
    wrap_text:bool = fields.Bool()
    bottom_label: Optional[str] = fields.Str(data_key='bottomLabel')
    on_click: Optional[OnClickSchema] = fields.Nested(OnClickSchema, data_key='onClick')
    button: Optional[ButtonSchema] = fields.Nested(ButtonSchema)
    switch_control: Optional[SwitchControlSchema] = fields.Nested(SwitchControlSchema, data_key='switchControl')
    end_icon: IconSchema =fields.Nested(IconSchema, data_key='endIcon')
