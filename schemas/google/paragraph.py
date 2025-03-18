from marshmallow import Schema, fields


class ParagraphSchema(Schema):

    text: str = fields.Str()
