from marshmallow import Schema, fields, validate


class BaseUserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate = validate.Length(min=6, max=255))


class PaymentReceiverLoginRequestSchema(BaseUserSchema):
    pass


class DataEntryLoginRequestSchema(BaseUserSchema):
    pass


class DataAnalystLoginRequestSchema(BaseUserSchema):
    pass


class AccountantLoginRegisterSchema(BaseUserSchema):
    pass


class CEOLoginRequestSchema(BaseUserSchema):
    pass


class BaseUserRegisterSchema(BaseUserSchema):
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    phone = fields.String(required=True, validate=validate.Length(min=13, max=13))


class DataEntryRegisterRequestSchema(BaseUserRegisterSchema):
    pass


class DataAnalystRegisterRequestSchema(BaseUserRegisterSchema):
    pass


class AccountantRegisterRequestSchema(BaseUserRegisterSchema):
    pass


class CEORegisterRequestSchema(BaseUserRegisterSchema):
    pass


class PaymentReceiverRegisterSchema(BaseUserRegisterSchema):
    iban = fields.String(required=True, validate=validate.Length(min=22, max=22))



