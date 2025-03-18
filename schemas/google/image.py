from typing import Literal, Optional
from marshmallow import Schema, fields

from .border import BorderStyleSchema
from .on_click import OnClickSchema


class ImageSchema(Schema):

    alt_text: Optional[str] = fields.Str(data_key='altText')
    image_url: str = fields.Str(data_key='imageUrl')
    on_click: Optional[OnClickSchema] = fields.Nested(OnClickSchema, data_key='onClick')


class ImageCropStyleSchema(Schema):

    aspect_ratio: Optional[float] = fields.Float(data_key='aspectRation')
    type: Literal['SQUARE', 'CIRCLE', 'RECTANGLE_CUSTOM', 'RECTANGLE_4_3'] = fields.Str()


class ImageComponentSchema(Schema):

    border_style: BorderStyleSchema = fields.Nested(BorderStyleSchema, data_key='borderStyle')
    crop_style: ImageCropStyleSchema = fields.Nested(ImageCropStyleSchema, data_key='cropStyle')
    alt_text: Optional[str] = fields.Str(data_key='altText')
    image_uri: str = fields.Str(data_key='imageUri')
