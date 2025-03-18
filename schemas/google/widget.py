
from typing import Optional
from marshmallow import Schema, fields

from .button import ButtonListSchema
from .column import ColumnsSchema
from .decorated_text import DecoratedTextSchema
from .grid import GridSchema
from .image import ImageSchema
from .input import DateTimePickerSchema, SelectionInputSchema, TextInputSchema
from .paragraph import ParagraphSchema

from ...dtos.google.literals import HorizontalAlignment


class WidgetSchema(Schema):

    button_list: Optional[ButtonListSchema] = fields.Nested(ButtonListSchema)
    columns: Optional[ColumnsSchema] = fields.Nested(ColumnsSchema)
    date_time_picker: Optional[DateTimePickerSchema] = fields.Nested(
        DateTimePickerSchema, data_key='dateTimePicker')
    decorated_text: Optional[DecoratedTextSchema]
    grid: Optional[GridSchema] = fields.Nested(GridSchema)
    horizontal_alignment: HorizontalAlignment = fields.Str(data_key='horizontalAlignment')
    selection_input: Optional[SelectionInputSchema] = fields.Nested(
        SelectionInputSchema, data_key='selectionInput')
    text_input: TextInputSchema = fields.Nested(TextInputSchema, data_key='textInput')
    text_paragraph: Optional[ParagraphSchema] = fields.Nested(ParagraphSchema, data_key='textParagraph')
    image: Optional[ImageSchema] = fields.Nested(ImageSchema)
    divider: dict[str, object] = fields.Dict()
