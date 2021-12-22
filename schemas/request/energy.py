from marshmallow import Schema, fields, validate


class BaseCreateRequestSchema(Schema):
    total_amount = fields.Integer(required=True)
    casting = fields.Integer(required=True)
    high_pressure_casting = fields.Integer(required=True)
    glazing = fields.Integer(required=True)
    sorting = fields.Integer(required=True)
    administration = fields.Integer(required=True)


class CompressorsCreateRequestSchema(Schema):
    total_amount = fields.Integer(required=True)
    compressor_one = fields.Integer(required=True)
    compressor_two = fields.Integer(required=True)
    compressor_three = fields.Integer(required=True)
    compressor_four = fields.Integer(required=True)
    compressor_five = fields.Integer(required=True)


class ElectricityCreateRequestSchema(BaseCreateRequestSchema):
    kilns = fields.Integer(required=True)
    shuttle_kilns = fields.Integer(required=True)


class NaturalGasCreateRequestSchema(BaseCreateRequestSchema):
    kilns = fields.Integer(required=True)
    shuttle_kilns = fields.Integer(required=True)


class WaterCreateRequestSchema(BaseCreateRequestSchema):
    pass
