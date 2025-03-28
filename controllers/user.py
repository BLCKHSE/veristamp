from flask import jsonify, request
from flask.views import MethodView

from ..dtos.google.action_render import ActionRender, Navigation
from ..dtos.google.general import General
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
            message = 'Invalid data provided, review and resubmit'
            navigation = Navigation(popToCard='get-started.registration')
        else:
            navigation = Navigation(update_card=self._subscription_plan_service.get_subscription_plan_card())

        render_action: ActionRender = ActionRender(navigation, message)

        return jsonify(self.response_schema.dump(render_action)), 200
