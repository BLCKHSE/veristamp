from marshmallow import EXCLUDE, Schema, ValidationError, fields, validate, validates

from ...database import db
from ...models.organisation import Organisation
from ...models.user import User


class UserRegistrationSchema(Schema):

    class Meta:
        unknown = EXCLUDE

    email = fields.Str(required=False)
    first_name = fields.Str(required=True, validate=[validate.Length(max=20, min=3)])
    last_name = fields.Str(required=False, validate=[validate.Length(max=20, min=1)])
    organisation = fields.Str(required=False, validate=[validate.Length(max=45, min=3)])

    @validates('email')
    def validate_email(self, value):
        if db.session.execute(db.select(User).filter_by(email=value)).one_or_none():
            raise ValidationError('email already in use')

    @validates('organisation')
    def validate_organisation(self, value):
        if db.session.execute(db.select(Organisation).filter_by(name=value)).one_or_none():
            raise ValidationError('organisation name already in use')
