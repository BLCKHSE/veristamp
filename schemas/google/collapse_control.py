from marshmallow import Schema, fields

from .button import ButtonSchema
from ...dtos.google.literals import HorizontalAlignment


class CollapseControlSchema(Schema):

    collapse_button: ButtonSchema = fields.Nested(ButtonSchema)
    expand_button: ButtonSchema = fields.Nested(ButtonSchema)
    horizontal_alignment: HorizontalAlignment = fields.Str(data_key='horizontalAlignment')
