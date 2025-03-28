from typing import List, Literal, Optional

from marshmallow import Schema,fields, post_load, validate

from ...dtos.google.action import Action

class ActionParameterSchema(Schema):

    key: str = fields.Str()
    value: str = fields.Str()

class ActionSchema(Schema):
    
    all_widgets_are_required: Optional[bool] = fields.Bool(data_key='allWidgetsAreRequired')
    function: Optional[str] = fields.Str()
    parameters: List[ActionParameterSchema] = fields.List(
        fields.Nested(ActionParameterSchema), required=False)
    load_indicator: Literal['SPINNER', 'NONE'] = fields.Str(
        data_key='loadIndicator',
        validate=[validate.OneOf(choices= ['SPINNER', 'NONE'])])
    persist_values: bool = fields.Bool(data_key='persistValues', dump_default=False)
    required_widgets: List[str] = fields.List(fields.Str(), data_key='requiredWidgets')
    interaction: Literal['INTERACTION_UNSPECIFIED', 'OPEN_DIALOG'] = fields.Str(
        validate=[validate.OneOf(choices= ['INTERACTION_UNSPECIFIED', 'OPEN_DIALOG'])],
        dump_default='INTERACTION_UNSPECIFIED'
    )

    @post_load
    def make_action(self, data, **kwargs):
        return Action(**data)
