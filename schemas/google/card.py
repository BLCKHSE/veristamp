from typing import List, Literal

from marshmallow import Schema, fields

from .input import SelectionInputSchema
from .section import SectionSchema
from .footer import FooterSchema
from .header import HeaderSchema
from .on_click import OnClickSchema


class CardAction(Schema):
    action_label: str = fields.Str(data_key='actionLabel')
    on_click: OnClickSchema = fields.Nested(OnClickSchema, data_key='onClick')


class CardSchema(Schema):

    card_actions: List[CardAction]
    fixed_footer: FooterSchema = fields.Nested(FooterSchema, data_key='fixedFooter')
    name: str = fields.Str()
    header: HeaderSchema = fields.Nested(HeaderSchema)
    peek_card_header: HeaderSchema = fields.Nested(HeaderSchema, data_key='peekCardHolder')
    sections: List[SectionSchema] = fields.List(fields.Nested(SectionSchema))
    display_style: Literal['PEEK', 'REPLACE'] = fields.Str(dump_default='REPLACE', data_key='displayStyle')
    section_divider_style: Literal['SOLID_DIVIDER', 'NO_DIVIDER'] = fields.Str(
        data_key='sectionDividerStyle',
        dump_default='SOLID_DIVIDER'
    )



class SelectionInputWidgetSuggestionsSchema(Schema):

    suggestions: List[SelectionInputSchema] = fields.List(fields.Nested(SelectionInputSchema))


class ModifyCardSchema(Schema):
    update_widget: SelectionInputWidgetSuggestionsSchema = fields.Nested(
        SelectionInputWidgetSuggestionsSchema, data_key='updateWidget')
