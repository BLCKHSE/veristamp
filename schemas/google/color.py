from marshmallow import Schema, fields


class ColorSchema(Schema):

    red: int = fields.Int()
    green: int = fields.Int()
    blue: int = fields.Int()
    alpha: int = fields.Int()
