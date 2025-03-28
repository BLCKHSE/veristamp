from typing import List

import requests

from ..models.subscriptions import SubscriptionOrganisation
from ..settings import PAYSTACK_SUBSCRIPTION_URI, PAYSTACK_BASE_URL, PAYSTACK_API_SECRET
from ..schemas.paystack.subscription import SubscriptionEventSchema

class PaystackService:

    def __init__(self):
        self._subscription_schema = SubscriptionEventSchema()

    def get_subscriptions(self, customer_id: str)-> List[SubscriptionOrganisation]:
        '''Fetches Paystack subscriptions tied to a customer_id
        
        Params:
            customer_id (str)
        '''
        try:
            subscriptions: List[SubscriptionOrganisation] = self._subscription_schema.load(
                data=requests.get(
                        url=f'{PAYSTACK_BASE_URL}{PAYSTACK_SUBSCRIPTION_URI}',
                        headers={'Authorization': f'Bearer {PAYSTACK_API_SECRET}'},
                        params={'customer': customer_id}
                    ),
                many=True
            )
            return subscriptions
        except Exception as ex:
            return []
