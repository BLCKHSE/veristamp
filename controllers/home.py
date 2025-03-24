import json
from typing import Optional
from flask import jsonify, request
from flask.views import MethodView

from ..database import db
from ..dtos.google.card import Card
from ..dtos.google.general import General
from ..models.user import User
from ..schemas.google.card import CardSchema
from ..schemas.google.general import GeneralSchema
from ..services.home import HomeService
from ..services.subscription import SubscriptionPlanService
from ..utils.decorators import authenticate

class HomeAPI(MethodView):

    init_every_request = False

    def __init__(self):
        super().__init__()
        self.request_schema = GeneralSchema()
        self.response_schema = CardSchema()

    @authenticate
    def post(self, **kwargs):
        payload: General = self.request_schema.load(request.get_json())
        email: str = payload.authorization_event_object.user_email
        user: Optional[User] = db.session.execute(db.select(User).filter_by(email=email)).one_or_none()

        card: Card = (
            HomeService().get_welcome_screen() 
            if user == None 
            else  SubscriptionPlanService().get_subscription_plan_card()
        )
        return jsonify(self.response_schema.dump(card)), 200
