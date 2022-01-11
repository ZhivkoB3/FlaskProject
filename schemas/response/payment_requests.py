from marshmallow import Schema, fields


class PaymentRequestsCreateResponseSchema(Schema):
    pk = fields.Integer(required=True)
    amount = fields.Integer(required=True)
    metric = fields.String(required=True)
    type = fields.String(required=True)
    total_invoice_amount = fields.Integer(required=True)
    created_on = fields.DateTime(required=True)
    user_id = fields.Integer(required=True)
    state = fields.String(required=True)
    updated_on = fields.DateTime(required=True)
    updated_by = fields.Integer(required=True)
