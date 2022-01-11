from marshmallow import Schema, fields


class PaymentRequestsCreateRequestSchema(Schema):
    amount = fields.Integer(required=True)
    metric = fields.String(required=True)
    type = fields.String(required=True)
    total_invoice_amount = fields.Integer(required=True)
