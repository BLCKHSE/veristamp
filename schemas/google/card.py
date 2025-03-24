from typing import List, Literal

from marshmallow import Schema, fields, post_load

from .input import SelectionInputSchema
from .section import SectionSchema
from .footer import FooterSchema
from .header import HeaderSchema
from .on_click import OnClickSchema
from ...dtos.google.card import Card, CardAction, ModifyCard, SelectionInputWidgetSuggestions


class CardActionSchema(Schema):
    action_label: str = fields.Str(data_key='actionLabel')
    on_click: OnClickSchema = fields.Nested(OnClickSchema, data_key='onClick')
    
    @post_load
    def make_card_action(self, data, **kwargs):
        return CardAction(**data)


class CardSchema(Schema):

    card_actions: List[CardActionSchema] = fields.Nested(CardActionSchema, data_key='cardActions')
    fixed_footer: FooterSchema = fields.Nested(FooterSchema, data_key='fixedFooter')
    name: str = fields.Str()
    header: HeaderSchema = fields.Nested(HeaderSchema)
    peek_card_header: HeaderSchema = fields.Nested(HeaderSchema, data_key='peekCardHeader')
    sections: List[SectionSchema] = fields.List(fields.Nested(SectionSchema))
    display_style: Literal['PEEK', 'REPLACE'] = fields.Str(dump_default='REPLACE', data_key='displayStyle')
    section_divider_style: Literal['SOLID_DIVIDER', 'NO_DIVIDER'] = fields.Str(
        data_key='sectionDividerStyle',
        dump_default='SOLID_DIVIDER'
    )

    @post_load
    def make_card(self, data, **kwargs):
        return Card(**data)


class SelectionInputWidgetSuggestionsSchema(Schema):

    suggestions: List[SelectionInputSchema] = fields.List(fields.Nested(SelectionInputSchema))

    @post_load
    def make_selection_input_suggestion(self, data, **kwargs):
        return SelectionInputWidgetSuggestions(**data)


class ModifyCardSchema(Schema):
    update_widget: SelectionInputWidgetSuggestionsSchema = fields.Nested(
        SelectionInputWidgetSuggestionsSchema, data_key='updateWidget')
    
    @post_load
    def make_modify_card(self, data, **kwargs):
        return ModifyCard(**data)
