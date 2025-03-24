from marshmallow import Schema, fields, post_load

from .button import ButtonSchema
from ...dtos.google.collapse_control import CollapseControl
from ...dtos.google.literals import HorizontalAlignment


class CollapseControlSchema(Schema):

    collapse_button: ButtonSchema = fields.Nested(ButtonSchema, data_key='collapseButton')
    expand_button: ButtonSchema = fields.Nested(ButtonSchema, data_key='expandButton')
    horizontal_alignment: HorizontalAlignment = fields.Str(data_key='horizontalAlignment')

    @post_load
    def make_collapse_control(self, data, **kwargs):
        return CollapseControl(**data)
