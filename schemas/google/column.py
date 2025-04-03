from typing import List, Literal, Optional

from marshmallow import Schema, fields

from .button import ButtonListSchema
from .chips import ChipListSchema
from .decorated_text import DecoratedTextSchema
from .image import ImageSchema
from .input import SelectionInputSchema, TextInputSchema
from .paragraph import ParagraphSchema
from ...dtos.google.literals import HorizontalAlignment, VerticalAlignment


class WidgetSchema(Schema):

    button_list: Optional[ButtonListSchema] = fields.Nested(ButtonListSchema, data_key='buttonList')
    chip_list: Optional[ChipListSchema] = fields.Nested(ChipListSchema, data_key='chipList')
    decorated_text: Optional[DecoratedTextSchema] = fields.Nested(DecoratedTextSchema, data_key='decoratedText')
    selection_input: Optional[SelectionInputSchema] = fields.Nested(SelectionInputSchema, data_key='selectionInput')
    text_input: TextInputSchema = fields.Nested(TextInputSchema, data_key='textInput')
    text_paragraph: Optional[ParagraphSchema] = fields.Nested(ParagraphSchema, data_key='textParagraph')
    image: Optional[ImageSchema] = fields.Nested(ImageSchema)


class ColumnItemSchema(Schema):

    horizontal_alignment: HorizontalAlignment = fields.Str(data_key='horizontalAlignment')
    horizontal_size_style: Literal['FILL_AVAILABLE_SPACE', 'FILL_MINIMUM_SPACE'] = fields.Str(data_key='horizontalSizeStyle')
    vertical_alignment: VerticalAlignment = fields.Str(data_key='verticalAlignment')
    widgets: List[WidgetSchema] = fields.List(fields.Nested(WidgetSchema))


class ColumnsSchema(Schema):

    column_items: List[ColumnItemSchema] = fields.List(fields.Nested(ColumnItemSchema), data_key='columnItems')
