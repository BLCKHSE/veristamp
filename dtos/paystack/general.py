from typing import Literal

Interval = Literal['weekly', 'monthly', 'quartely', 'biannually', 'annually']

SubscriptionStatus = Literal['active', 'non_renewing', 'attention', 'completed', 'cancelled']
