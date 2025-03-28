from flask import jsonify, request
from flask.views import MethodView

from ..dtos.paystack.subscriptions import SubscriptionEventDTO
from ..services.subscription import SubscriptionPaymentService, SubscriptionService
from ..schemas.paystack.subscription import SubscriptionEventSchema
from ..utils.decorators import authenticate_paystack
from ..utils.enums import PaystackEvent


class SubscriptionAPI(MethodView):
    
    init_every_request = False

    def __init__(self):
        self.request_schema = SubscriptionEventSchema()
        self._subscription_service = SubscriptionService()
        self._subscription_payment_service = SubscriptionPaymentService()

    @authenticate_paystack
    def post(self, **kwargs):
        event: SubscriptionEventDTO = self.request_schema.load(request.get_json())
        if event.event == PaystackEvent.SUBSCRIPTION_CREATE.value:
            self._subscription_service.create_subscription_paystack(event.data)
        elif event.event == PaystackEvent.CHARGE_SUCCESS.value:
            self._subscription_payment_service.create_payment_paystack(event.data)

        return jsonify({}), 200
