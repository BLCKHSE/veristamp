from typing import Optional

from ..models.organisation import Organisation
from ..utils.enums import BusinessCategory


class OrganisationService:

    def create(self, name: str, category: BusinessCategory, website: Optional[str]) -> Organisation :
        organisation: Organisation = Organisation(name, category, website)
        organisation.save()

        return organisation
