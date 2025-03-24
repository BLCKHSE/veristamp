from typing import List

from ..database import db
from ..dtos.google.button import Button, ButtonList
from ..dtos.google.card import Card
from ..dtos.google.decorated_text import DecoratedText
from ..dtos.google.header import Header
from ..dtos.google.icon import Icon, MaterialIcon
from ..dtos.google.image import Image
from ..dtos.google.link import OpenLink
from ..dtos.google.on_click import OnClick
from ..dtos.google.section import Section
from ..dtos.google.widget import Widget
from ..models.subscriptions import SubscriptionPlan
from ..schemas.google.card import CardSchema
from ..utils.enums import Status


class SubscriptionPlanService:

    def __init__(self):
        self._response_schema = CardSchema()

    def _get_period(self, days: int) -> str:
        period: str = 'mo'
        if days >= 365:
            period = 'yr'
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
                on_click= OnClick(open_link= OpenLink(plan.plan_url))
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
            name='get-started.subscription_plans',
            header=Header('Simple Pricing for Compliant Digital Stamps'),
            sections=[sub_plan_section]
        )
        return card
