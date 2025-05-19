from typing import List, Literal, Optional
from marshmallow import EXCLUDE, Schema, fields

from .card import CardSchema, ModifyCardSchema
from .link import LinkPreviewSchema, LinkSchema, OpenLinkSchema


class ActionNavigationSchema(Schema):

    action: Literal['CLOSE_DIALOG', 'CLOSE_DIALOG_AND_EXECUTE'] = fields.Str()


class ActionNotificationSchema(Schema):

    text: str = fields.Str()


class NavigationSchema(Schema):

    pop_to_root: bool = fields.Bool(data_key='popToRoot')
    pop: bool = fields.Bool()
    pop_to_card: bool = fields.Bool(data_key='popToCard')
    push_card: CardSchema = fields.Nested(CardSchema, data_key='pushCard')
    update_card: CardSchema = fields.Nested(CardSchema, data_key='updateCard')
    end_navigation: ActionNavigationSchema = fields.Nested(ActionNavigationSchema, data_key='endNavigation')


class ActionRenderActionSchema(Schema):

    link: Optional[OpenLinkSchema] = fields.Nested(OpenLinkSchema)
    links: Optional[List[LinkSchema]] = fields.Nested(LinkSchema)
    link_preview: LinkPreviewSchema = fields.Nested(LinkPreviewSchema, data_key='linkPreview')
    modify_operations: List[ModifyCardSchema] = fields.List(
        fields.Nested(ModifyCardSchema), data_key='modifyOperations')
    navigations: List[NavigationSchema] = fields.List(fields.Nested(NavigationSchema))
    notification: ActionNotificationSchema = fields.Nested(ActionNotificationSchema)


class ActionRenderSchema(Schema):

    class Meta:
        unknown = EXCLUDE

    action: ActionRenderActionSchema = fields.Nested(ActionRenderActionSchema )
    host_app_action: object = fields.Dict(data_key='hostAppAction')
    schema: Optional[str] = fields.Str()
