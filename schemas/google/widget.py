
from typing import Optional
from marshmallow import Schema, fields, post_dump, post_load

from .button import ButtonListSchema
from .chips import ChipListSchema
from .column import ColumnsSchema
from .decorated_text import DecoratedTextSchema
from .grid import GridSchema
from .image import ImageSchema
from .input import DateTimePickerSchema, SelectionInputSchema, TextInputSchema
from .paragraph import ParagraphSchema
from ...dtos.google.literals import HorizontalAlignment
from ...dtos.google.widget import Widget


class WidgetSchema(Schema):

    button_list: Optional[ButtonListSchema] = fields.Nested(ButtonListSchema, data_key='buttonList')
    chip_list: Optional[ChipListSchema] = fields.Nested(ChipListSchema, data_key='chipList')
    columns: Optional[ColumnsSchema] = fields.Nested(ColumnsSchema)
    date_time_picker: Optional[DateTimePickerSchema] = fields.Nested(
        DateTimePickerSchema, data_key='dateTimePicker')
    decorated_text: Optional[DecoratedTextSchema] = fields.Nested(DecoratedTextSchema, data_key='decoratedText')
    grid: Optional[GridSchema] = fields.Nested(GridSchema)
    horizontal_alignment: HorizontalAlignment = fields.Str(data_key='horizontalAlignment')
    selection_input: Optional[SelectionInputSchema] = fields.Nested(
        SelectionInputSchema, data_key='selectionInput')
    text_input: TextInputSchema = fields.Nested(TextInputSchema, data_key='textInput')
    text_paragraph: Optional[ParagraphSchema] = fields.Nested(ParagraphSchema, data_key='textParagraph')
    image: Optional[ImageSchema] = fields.Nested(ImageSchema)
    divider: dict[str, object] = fields.Dict()

    @post_load
    def make_widget(self, data, **kwargs):
        return Widget(**data)
    
    # TODO: Move to abstract class
    @post_dump
    def remove_empty_values(self, data, **_):
        return {
            key: value for key, value in data.items()
            if value is not None
        }
