import json
from typing import List

from marshmallow import EXCLUDE, Schema, ValidationError, fields, validate, validates
from werkzeug.datastructures import FileStorage

from ...utils.enums import StampShape, StampTemplateKey

class TemplateMetadataSchema(Schema):

    class Meta:
        unknown = EXCLUDE

    key: StampTemplateKey = fields.Enum(StampTemplateKey, required=True)
    max_size: int = fields.Integer(validate=validate.Range(3,30), data_key='maxSize', required=True)


class TemplateSchema(Schema):

    class Meta:
        unknown = EXCLUDE

    name: str = fields.String(validate=validate.Length(min=3, max=20), required=True)
    description: str = fields.String(validate=validate.Length(min=3, max=60), required=True)
    shape: StampShape = fields.Enum(StampShape, by_value=True, required=True)
    image_url: str = fields.Str(dump_only=True, data_key='imageUrl')
    template_metadata: List[TemplateMetadataSchema] = fields.Nested(TemplateMetadataSchema, dump_only=True, data_key='templateMetadata')
    metadata: str = fields.String(required=True, load_only=True)

    @validates('metadata')
    def validate_metadata(self, value: str):
        try:
            metadata_list: list[dict[str, object]] = json.loads(value)
            if len(metadata_list) < 0 or len(metadata_list) > 10:
                raise ValidationError('List length must be greater than 0 and less than 10')
            errors: dict[str, list[str]] = TemplateMetadataSchema().validate(metadata_list, many=True)
            if len(errors) > 0:
                raise ValidationError(errors)
        except json.JSONDecodeError:
            raise ValidationError('Invalid list provided')


class TemplateFileSchema(Schema):

    class Meta:
        unknown = EXCLUDE

    file: FileStorage = fields.Raw(type='file', required=True)

    @validates('file')
    def validate_file(self, value: FileStorage):
        file_type: str = value.content_type
        if file_type != 'image/svg+xml':
            raise ValidationError('Invalid file type. Must be SVG.')
