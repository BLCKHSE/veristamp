from marshmallow import Schema, fields

from .action import ActionSchema
from ...dtos.google.literals import ControlType


class SwitchControlSchema(Schema):

    control_type: ControlType = fields.Str(data_key='controlType')
    name: str = fields.Str()
    value: str = fields.Str()
    selected: bool = fields.Bool()
    on_change_action: ActionSchema = fields.Nested(ActionSchema , data_key='onChangeAction')
