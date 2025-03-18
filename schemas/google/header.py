
from typing import Optional
from marshmallow import Schema, fields

from ...dtos.google.literals import ImageType


class HeaderSchema(Schema):

    title: str = fields.Str(required=True)
    subtitle: Optional[str] = fields.Str()
    image_url: Optional[str] = fields.Str(data_key='imageUrl')
    image_type: ImageType = fields.Str()
