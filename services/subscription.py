from typing import List, Optional, Tuple

from .paystack import PaystackService
from .user import UserService
from ..database import db
from ..dtos.google.action import Action, ActionParameter
from ..dtos.google.button import Button, ButtonList
from ..dtos.google.card import Card
from ..dtos.google.decorated_text import DecoratedText
from ..dtos.google.footer import Footer
from ..dtos.google.header import Header
from ..dtos.google.icon import Icon, MaterialIcon
from ..dtos.google.image import Image
from ..dtos.google.link import OpenLink
from ..dtos.google.on_click import OnClick
from ..dtos.google.section import Section
from ..dtos.google.widget import Widget
from ..dtos.paystack.subscriptions import SubscriptionEventDataDTO
from ..models.subscriptions import SubscriptionOrganisation, SubscriptionPayment, SubscriptionPlan
from ..models.user import User
from ..settings import BASE_URL
from ..utils.enums import Status


class SubscriptionPaymentService:

    def __init__(self):
        self._paystack_service = PaystackService()
        self._subscription_service = SubscriptionService()
        self._subscription_plan_service = SubscriptionPlanService()
        self._user_service = UserService()

    def create_payment_paystack(self, subsciption_event_data: SubscriptionEventDataDTO) -> Tuple[SubscriptionPayment, Optional[dict[str, str]]]:
        '''Creates a SubscriptionOrganisation record from a Paystack subscription creation webhook

            Parameters:
                self (SubscriptionService)
                subscription_event_data (SubscriptionEventDataDTO)
            Returns:
                object
        '''
        user: User = self._user_service.get_user(subsciption_event_data.customer.email)
        if user == None:
            return None, {'user': 'User not found'}
        subscription = self._subscription_service.get_subscription(organisation_id=user.organisation_id)
        if subscription == None:
            subscription_data: List[SubscriptionEventDataDTO] = self._paystack_service.get_subscription(user.paystack_customer_id)
            if subscription_data.count() == 0:
                return None, {'subscription': 'Subscription not found'}
            subscription =  self._subscription_service.create(subsciption_event_data=subscription_data[0], organisation_id=user.organisation_id)

        subscription_payment: SubscriptionPayment = SubscriptionPayment(
            subsciption_data=subsciption_event_data, 
            subscription_id=subscription.id
        )
        subscription_payment.save()

        return subscription_payment, None

class SubscriptionPlanService:

    HOME_URL = f'{BASE_URL}/api/home'
    CARD_ID = 'get-started.subscription_plans'

    def _get_confirm_subscription_btn(self, card_id: Optional[str] = CARD_ID) -> Button:
        '''Gets confirm subscription payment completed button.
            Called to check subscription created successfully
        '''
        on_click_obj: OnClick = OnClick(
            Action(
                self.HOME_URL,
                parameters=[ActionParameter('source_id', card_id)],
            )
        )
        confirm_button: Button = Button(
            'Confirm Subscription Activated', 
            'CONFIRM',
            on_click_obj,
            type='OUTLINED'
        )
        
        return confirm_button

    def _get_period(self, days: int) -> str:
        '''Gets period representation based on days count'''
        period: str = 'mo'
        if days == 365:
            period = 'yr'
        elif days == 7:
            period = 'wk'
        return period

    def _get_subscription_plan_features(self, features: List[str]) -> List[Widget]:
        feature_widgets: List[Widget] = []
        for feat in features:
            text_widget: DecoratedText = DecoratedText(
                feat, 
                start_icon=Icon(material_icon=MaterialIcon('check_small')),
                wrap_text=True
            )
            feature_widgets.append(Widget(decorated_text=text_widget))
        return feature_widgets

    def get_subscription_plans(self) -> List[SubscriptionPlan]:
        return db.session.scalars(db.select(SubscriptionPlan).filter_by(status=Status.ACT)).all()
    
    def get_subscription_plan(self, subscription_id: str) -> Optional[SubscriptionPlan]:
        return db.session.scalars(
            db.select(SubscriptionPlan).filter_by(provider_plan_id=subscription_id)).one_or_none()

    def get_subscription_plan_card(self) -> Card:

        sub_plans: List[SubscriptionPlan] = self.get_subscription_plans()
        sub_plan_widgets: List[Widget] = []
        for plan in sub_plans:
            sub_plan_image: Image = Image(f'{plan.name} image', plan.image_url)
            btn_txt: str = f'''GET STARTED - {plan.currency.value.upper()}
                {plan.price}/{self._get_period(plan.period_in_days)}'''
            sub_plan_btn: Button = Button(
                alt_text=f'{plan.name} image',
                text=btn_txt,
                on_click= OnClick(open_link= OpenLink(plan.plan_url)),
            )
            sub_plan_btns: ButtonList = ButtonList([sub_plan_btn])
            sub_plan_widgets.extend([
                Widget(image=sub_plan_image),
                *self._get_subscription_plan_features(plan.features),
                Widget(button_list=sub_plan_btns), 
            ])
            sub_plan_widgets.append(Widget(divider={}))

        sub_plan_section: Section = Section(
            header='<font color=\'#35446D\'>Choose a Package That Works for You</font>',
            widgets=sub_plan_widgets
        )

        card: Card = Card(
            name=self.CARD_ID,
            header=Header('Simple Pricing for Compliant Digital Stamps'),
            sections=[sub_plan_section],
            fixed_footer=Footer(self._get_confirm_subscription_btn())
        )
        return card


class SubscriptionService:
    '''Organisation subscriptions service'''

    def __init__(self):
        self._user_service = UserService()
        self._subscription_plan_service = SubscriptionPlanService()

    def create(self, subsciption_event_data: SubscriptionEventDataDTO, organisation_id: str) -> SubscriptionOrganisation:
        sub_plan: SubscriptionPlan = self._subscription_plan_service.get_subscription_plan(
            subsciption_event_data.plan.plan_code)
        sub_org: SubscriptionOrganisation = SubscriptionOrganisation(
            subsciption_event_data, 
            organisation_id,
            sub_plan.id
        )
        sub_org.save()
        return sub_org

    def create_subscription_paystack(self, subsciption_event_data: SubscriptionEventDataDTO) -> Optional[SubscriptionOrganisation]:
        '''Creates a SubscriptionOrganisation record from a Paystack subscription creation webhook

            Parameters:
                self (SubscriptionService)
                subscription_event (SubscriptionEventDTO)
            Returns:
                Optional[SubscriptionOrganisation]
        '''
        user: User = self._user_service.get_user(subsciption_event_data.customer.email)
        if user != None:
            return self.create(subsciption_event_data=subsciption_event_data, organisation_id=user.organisation_id)

        return None

    def get_subscription(self, organisation_id: str) -> Optional[SubscriptionOrganisation]:
        return db.session.scalar(db.select(SubscriptionOrganisation).filter_by(organisation_id=organisation_id))
