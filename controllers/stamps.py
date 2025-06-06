from typing import Dict, Optional, Tuple

from flask import jsonify, render_template, request
from flask.views import MethodView

from ..data.constants import CARD_ID_CREATE_STAMP, CARD_ID_HOME, STAMPS_WEB_PREVIEW_URI
from ..dtos.google.action_render import ActionRender, Navigation
from ..dtos.google.card import Card
from ..dtos.google.doc import Doc
from ..dtos.google.general import General
from ..dtos.google.literals import GoogleSource
from ..models.stamps import Stamp, StampTemplate
from ..models.user import User
from ..schemas.google.action_render_schema import ActionRenderSchema
from ..schemas.google.general import GeneralSchema
from ..services.home import HomeService
from ..services.stamps import StampService
from ..services.templates import TemplateService
from ..services.user import UserService
from ..settings import BASE_URL, THEME_PRIMARY_COLOUR
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
        '''Create stamp endpoint'''
        payload: General = self._general_schema.load(request.get_json())
        source: GoogleSource = payload.common_event_object.source
        template_id: str = payload.common_event_object.parameters.get('template_id')
        user_email: str = payload.authorization_event_object.user_email
        result: Tuple[Stamp, dict[str, str]] = self._stamp_service.create(
            template_id=template_id,
            form_inputs=payload.common_event_object.form_inputs,
            creator_email=user_email
        )
        stamp: Stamp = result[0]
        errors: Dict[str, str] = result[1]
        navigation: Navigation = None

        if errors != None and len(errors) > 0:
            message = 'Invalid data provided, review and resubmit'
            navigation = Navigation(pop_to_card=CARD_ID_CREATE_STAMP)
        else:
            navigation = Navigation(update_card=self._home_service.get_home_card(stamp.creator, source))
        message: str = f'Yay! Stamp \'{stamp.name}\', successfully created'
        render_action: ActionRender = ActionRender(navigation=navigation, notification_msg=message)

        return jsonify(self._action_render_schema.dump(render_action)), 200


class StampApplyApi(MethodView):

    init_every_request = False

    def __init__(self):
        super().__init__()
        self._action_render_schema = ActionRenderSchema()
        self._general_schema = GeneralSchema()
        self._stamp_service = StampService()
        self._stamp_template_service = TemplateService()
        self._user_service = UserService()

    @authenticate
    def post(self, **kwargs):
        payload: General = self._general_schema.load(request.get_json())
        source: GoogleSource = payload.common_event_object.source
        stamp_id: str = payload.common_event_object.parameters.get('grid_item_identifier', None)

        stamp: Optional[Stamp] = self._stamp_service.get_stamp(stamp_id)
        user: Optional[User] = self._user_service.get_user(payload.authorization_event_object.user_email)
        navigation: Navigation = None
        message: str = None
        if stamp == None:
            message = 'Failed to load stamp'
            navigation: Navigation = Navigation(pop_to_card=CARD_ID_HOME)
        else:
            stamp_template: Optional[StampTemplate] = self._stamp_template_service.get_template(stamp.template_id)
            
            apply_stamp_card: Optional[Card] = self._stamp_service.get_apply_stamp_card(
                template=stamp_template,
                stamp=stamp,
                user=user,
                source=source
            )
            navigation = Navigation(push_card=apply_stamp_card) if apply_stamp_card != None else Navigation(pop_to_card=CARD_ID_HOME)
        
        render_action: ActionRender = ActionRender(navigation=navigation, notification_msg=message)

        return jsonify(self._action_render_schema.dump(render_action)), 200


class StampApplyDocApi(MethodView):

    init_every_request = False

    def __init__(self):
        super().__init__()
        self._action_render_schema = ActionRenderSchema()
        self._general_schema = GeneralSchema()
        self._home_service = HomeService()
        self._stamp_service = StampService()
        self._user_service = UserService()

    @authenticate
    def post(self, **kwargs):
        payload: General = self._general_schema.load(request.get_json())
        source: GoogleSource = payload.common_event_object.source
        stamp_url: str = payload.common_event_object.parameters.get('stamp_url')
        stamp_id: str = payload.common_event_object.parameters.get('stamp_id')
        success: bool = request.args.get('success', False)
        user: User = self._user_service.get_user(payload.authorization_event_object.user_email)
        if success:
            self._stamp_service.apply_stamp(payload.docs, user, stamp_url, stamp_id)

        navigation: Navigation = Navigation(update_card=self._home_service.get_home_card(user, source))
        message: str = 'Stamp successfully Applied' if success else 'Failed to apply stamp'
        render_action: ActionRender = ActionRender(navigation=navigation, notification_msg=message)

        return jsonify(self._action_render_schema.dump(render_action)), 200
    
    def get(self):
        '''Handles Download Stamp Flow'''

        stamp_url: str = request.args.get('stamp_url')
        stamp_id: str = request.args.get('stamp_id')

        return render_template('stamp_download.html', stamp_url=stamp_url)
class StampPreviewApi(MethodView):

    init_every_request = False

    def __init__(self):
        super().__init__()
        self._action_render_schema = ActionRenderSchema()
        self._general_schema = GeneralSchema()
        self._stamp_service = StampService()

    @authenticate
    def post(self, **kwargs):
        '''Create stamp endpoint'''
        payload: General = self._general_schema.load(request.get_json())
        user_email: str = payload.authorization_event_object.user_email
        template_id: str = payload.common_event_object.parameters.get('template_id')
        cache_key: str = self._stamp_service.set_preview_data(
            template_id=template_id,
            form_inputs=payload.common_event_object.form_inputs,
            creator_email=user_email,
        )
        render_action: ActionRender = ActionRender(link=f'{BASE_URL}{STAMPS_WEB_PREVIEW_URI}/{cache_key}')

        return jsonify(self._action_render_schema.dump(render_action)), 200


class StampWebApi(MethodView):

    init_every_request = False

    def __init__(self):
        super().__init__()
        self._request_schema = GeneralSchema()
        self._stamp_service = StampService()
        self._template_service = TemplateService()
        self._user_service = UserService()

    def get(self, stamp_preview_key: str,  **kwargs):
        data: Optional[Dict[str, str]] = self._stamp_service.get_preview_data(stamp_preview_key)
        if data == None:
            return render_template('stamp_preview.html', success=False)
        user: User = self._user_service.get_user(data.get('user_email'))
        timezone: str = user.timezone if user != None else None
        template: StampTemplate = self._template_service.get_template(data.get('template_id'))
        stamp: str = self._stamp_service.get_variable_filled_stamp(
            template=template, inputs=data.get('content'), timezone=timezone
        )
        stamp = stamp.replace(THEME_PRIMARY_COLOUR, data.get('colour'))
        content: Dict[str, str] = {
            'success': True,
            'name': data.get('stamp_name'),
            'user': data.get('email'),
            'template_id': data.get('template_id'),
            'stamp': stamp,
            'content': data.get('content')
        }

        return render_template('stamp_preview.html', **content)
