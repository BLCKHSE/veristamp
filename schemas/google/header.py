from typing import Optional
from marshmallow import Schema, fields, post_load

from ...dtos.google.header import Header
from ...dtos.google.literals import ImageType


class HeaderSchema(Schema):

    title: str = fields.Str(required=True)
    subtitle: Optional[str] = fields.Str()
    image_url: Optional[str] = fields.Str(data_key='imageUrl')
    image_type: ImageType = fields.Str(data_key='imageType')

    @post_load
    def make_header(self, data, **kwargs):
        return Header(**data)
