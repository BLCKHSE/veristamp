from typing import Dict, Optional, Tuple

from ..database import db
from ..dtos.google.general import FormInput, General
from ..models.organisation import Organisation
from ..models.user import User
from ..services.organisation import OrganisationService
from ..schemas.users.user import UserRegistrationSchema
from ..utils.enums import UserRole


class UserService:

    def __init__(self):
        self._schema = UserRegistrationSchema()

    def create(self, general: General) -> Tuple[User, Optional[dict[str, str]]]:
        form_inputs: dict[str, FormInput] = general.common_event_object.form_inputs
        data: Dict[str, object] = {
            'email': general.authorization_event_object.user_email,
            'first_name': form_inputs.get('first_name').stringInputs.value[0],
            'last_name': form_inputs.get('last_name').stringInputs.value[0],
            'organisation': form_inputs.get('organisation').stringInputs.value[0],
            'time_zone': general.common_event_object.time_zone.id
        }
        errors: dict[str, str] = self._schema.validate(data)
        user: User = None
        if errors == None or len(errors) == 0:
            organisation: Organisation = OrganisationService().create(
                name=form_inputs.get('organisation').stringInputs.value[0],
                category=form_inputs.get('category').stringInputs.value[0],
                website=form_inputs.get('website_url').stringInputs.value[0] if form_inputs.get('website_url') else None
            )
            user = User(data)
            user.organisation_id = organisation.id
            user.role = UserRole.OWN
            user.save()

        return user, errors
    
    def get_user(self, email: str) -> Optional[User]:
        return db.session.scalars(db.select(User).filter_by(email=email)).one_or_none()
