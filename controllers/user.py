from flask import jsonify, request
from flask.views import MethodView

from ..dtos.google.action_render import ActionRender, Navigation
from ..dtos.google.card import Card
from ..dtos.google.general import General
from ..dtos.google.literals import GoogleSource
from ..services.onboard import OnboardService
from ..services.subscription import SubscriptionPlanService
from ..services.user import UserService
from ..schemas.google.action_render_schema import ActionRenderSchema
from ..schemas.google.general import GeneralSchema
from ..schemas.users.user import UserRegistrationSchema
from ..utils.decorators import authenticate


class UserAPI(MethodView):
    
    # only 1 instance created for all requests so avoid saving to self, use g instead
    init_every_request = False

    def __init__(self):
        self.request_schema = GeneralSchema()
        self.validation_schema = UserRegistrationSchema()
        self.response_schema = ActionRenderSchema() 
        self._service = UserService()
        self._subscription_plan_service = SubscriptionPlanService()

    @authenticate
    def post(self, **kwargs):
        payload: General = self.request_schema.load(request.get_json())
        _, errors = self._service.create(payload)
        navigation: Navigation = None
        message: str = 'Woohoo! Your VERISTAMP account has been successfully created'
        if errors != None and len(errors) > 0:
            error_msgs: str = ','.join([value for key, value in errors])
            message = f'Invalid data provided, review and resubmit\n{error_msgs}'
            navigation = Navigation(pop_to_card='get-started.registration')
        else:
            navigation = Navigation(update_card=self._subscription_plan_service.get_subscription_plan_card())

        render_action: ActionRender = ActionRender(navigation, message)

        return jsonify(self.response_schema.dump(render_action)), 200

class OnboardAPI(MethodView):
    
    init_every_request = False

    def __init__(self):
        super().__init__()
        self._action_render_schema = ActionRenderSchema()
        self._general_schema = GeneralSchema()
        self._onboard_service = OnboardService()

    @authenticate
    def post(self, **kwargs):

        payload: General = self._general_schema.load(request.get_json())
        source: GoogleSource = payload.common_event_object.source
        card: Card = self._onboard_service.get_registration_card(source)
        render_action: ActionRender = ActionRender(navigation=Navigation(update_card=card))

        return jsonify(self._action_render_schema.dump(render_action)), 200
