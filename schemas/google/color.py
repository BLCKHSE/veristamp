from marshmallow import Schema, fields, post_load

from ...dtos.google.color import Color


class ColorSchema(Schema):

    red: float = fields.Float()
    green: float = fields.Float()
    blue: float = fields.Float()
    alpha: int = fields.Int()

    @post_load
    def make_color(self, data, **kwargs):
        return Color(**data)

