from marshmallow import Schema, fields


class BaseCreateRequestSchema(Schema):
    casting = fields.Integer(required=True)
    high_pressure_casting = fields.Integer(required=True)
    glazing = fields.Integer(required=True)
    sorting = fields.Integer(required=True)
    administration = fields.Integer(required=True)


class CompressorsCreateRequestSchema(Schema):
    total_kwh = fields.Integer(required=True)
    compressor_one = fields.Integer(required=True)
    compressor_two = fields.Integer(required=True)
    compressor_three = fields.Integer(required=True)
    compressor_four = fields.Integer(required=True)
    compressor_five = fields.Integer(required=True)


class ElectricityCreateRequestSchema(BaseCreateRequestSchema):
    total_kwh = fields.Integer(required=True)
    kilns = fields.Integer(required=True)
    shuttle_kilns = fields.Integer(required=True)


class NaturalGasCreateRequestSchema(BaseCreateRequestSchema):
    total_Nm3 = fields.Integer(required=True)
    kilns = fields.Integer(required=True)
    shuttle_kilns = fields.Integer(required=True)


class WaterCreateRequestSchema(BaseCreateRequestSchema):
    total_m3 = fields.Integer(required=True)
