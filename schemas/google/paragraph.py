from marshmallow import Schema, fields, post_load

from ...dtos.google.paragraph import Paragraph


class ParagraphSchema(Schema):

    text: str = fields.Str()

    @post_load
    def make_paragraph(self, data, **kwargs):
        return Paragraph(**data)
