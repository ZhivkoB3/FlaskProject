from marshmallow import Schema, fields


class BaseUserResponseSchema(Schema):
    role = fields.String(required=True)