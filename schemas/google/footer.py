from marshmallow import Schema, fields

from .button import ButtonSchema


class FooterSchema(Schema):
    primary_button: ButtonSchema = fields.Nested(ButtonSchema)
    secondary_button: ButtonSchema = fields.Nested(ButtonSchema)
