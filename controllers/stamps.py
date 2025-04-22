from typing import Dict, Tuple
from flask import jsonify, request
from flask.views import MethodView

from ..data.constants import CARD_ID_CREATE_STAMP
from ..dtos.google.action_render import ActionRender, Navigation
from ..dtos.google.general import General
from ..models.stamps import Stamp
from ..schemas.google.action_render_schema import ActionRenderSchema
from ..schemas.google.general import GeneralSchema
from ..services.home import HomeService
from ..services.stamps import StampService
from ..utils.decorators import authenticate


class  StampAddonApi(MethodView):
    
    init_every_request = False

    def __init__(self):
        super().__init__()
        self._action_render_schema = ActionRenderSchema()
        self._general_schema = GeneralSchema()
        self._home_service = HomeService()
        self._stamp_service = StampService()

    @authenticate
    def post(self, **kwargs):
        payload: General = self._general_schema.load(request.get_json())
        template_id: str = request.args.get('t_id')
        user_email: str = kwargs.get('user_email')
        result: Tuple[Stamp, dict[str, str]] = self._stamp_service.create(
            template_id=template_id,
            form_inputs=payload.common_event_object.form_inputs,
            creator_email=user_email
        )
        stamp: Stamp = result[0]
        errors: Dict[str, str] = result[1]
        navigation: Navigation = None

        if result[1] != None and len(errors) > 0:
            message = 'Invalid data provided, review and resubmit'
            navigation = Navigation(popToCard=CARD_ID_CREATE_STAMP)
        else:
            navigation = Navigation(update_card=self._home_service.get_home_card(stamp.creator))
        message: str = f'Yay! Stamp {stamp.name}, successfully created'
        render_action: ActionRender = ActionRender(navigation, message)

        return jsonify(self._action_render_schema.dump(render_action)), 200
