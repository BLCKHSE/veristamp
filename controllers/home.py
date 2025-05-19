from typing import Optional

from flask import jsonify, request
from flask.views import MethodView

from ..database import db
from ..dtos.google.action_render import ActionRender, Navigation
from ..dtos.google.card import Card
from ..dtos.google.general import General
from ..dtos.google.literals import GoogleSource
from ..models.subscriptions import SubscriptionOrganisation
from ..models.user import User
from ..schemas.google.action_render_schema import ActionRenderSchema
from ..schemas.google.card import CardSchema
from ..schemas.google.general import GeneralSchema
from ..services.home import HomeService
from ..services.onboard import OnboardService
from ..services.subscription import SubscriptionPlanService, SubscriptionService
from ..utils.decorators import authenticate

class HomeAPI(MethodView):

    init_every_request = False

    def __init__(self):
        super().__init__()
        self._action_render_schema = ActionRenderSchema()
        self.request_schema = GeneralSchema()
        self.response_schema = CardSchema()
        self._home_service = HomeService()
        self._onboard_service = OnboardService()
        self._subscription_service = SubscriptionService()

    @authenticate
    def post(self, **kwargs):

        payload: General = self.request_schema.load(request.get_json())
        email: str = payload.authorization_event_object.user_email if payload.authorization_event_object != None else None
        referrer: str = payload.common_event_object.parameters.get('referrer', 'link')
        source: GoogleSource = payload.common_event_object.source
        user: Optional[User] = db.session.scalar(db.select(User).filter_by(email=email))

        if user == None:
            return self._onboard_service.get_welcome_screen(source)

        org_subscription: SubscriptionOrganisation = self._subscription_service.get_subscription(user.organisation_id)
        card: Card = (
            self._home_service.get_home_card(user, source)
            if org_subscription != None
            else  SubscriptionPlanService().get_subscription_plan_card()
        )

        if referrer == 'nav':
            return jsonify(self._action_render_schema.dump(ActionRender(Navigation(update_card=card))))

        return jsonify(self.response_schema.dump(card)), 200
