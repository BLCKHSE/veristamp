from datetime import datetime
from os import getenv

import jwt
from marshmallow import EXCLUDE, Schema, ValidationError, fields, pre_load, validates_schema


class Auth(Schema):

    class Meta:
        unknown = EXCLUDE

    client_id: str = fields.Str()
    expiry_timestamp: datetime = fields.DateTime()
    issuer: str = fields.Str()
    system_id_token: str = fields.Str(required=True, data_key='systemIdToken')
    user_o_auth_token: str = fields.Str(required=True, data_key='userOAuthToken')
    user_email: str = fields.Str(allow_none=True)
    user_id_token: str = fields.Str(required=True, data_key='userIdToken')
    email_verified: bool = fields.Bool(allow_none=True)

    @pre_load
    def process_user(self, data, **kwargs):
        decodedToken: dict[str, object] = jwt.decode(data.get('userIdToken'), options={'verify_signature': False})
        self.client_id = decodedToken.get('aud')
        self.issuer = decodedToken.get('iss')
        self.expiry_timestamp = datetime.fromtimestamp(decodedToken.get('exp'))
        data['user_email'] = decodedToken.get('email')
        data['email_verified'] = decodedToken.get('email_verified')
        return data


    @validates_schema
    def validate_auth(self, data, **kwargs):
        if (
            getenv('GOOGLE_CLIENT_ID') != self.client_id 
            or getenv('GOOGLE_ISSUER') != self.issuer
            or self.expiry_timestamp < datetime.now()
        ):
            raise ValidationError('unauthorised access')
