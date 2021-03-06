from marshmallow import Schema, fields


class BaseEnergyCreateResponseSchema(Schema):
    pk = fields.Integer(required=True)
    casting = fields.Integer(required=True)
    high_pressure_casting = fields.Integer(required=True)
    glazing = fields.Integer(required=True)
    sorting = fields.Integer(required=True)
    administration = fields.Integer(required=True)
    created_on = fields.DateTime(required=True)
    data_entry_id = fields.Integer(required=True)


class CompressorsCreateResponseSchema(Schema):
    pk = fields.Integer(required=True)
    total_kwh = fields.Integer(required=True)
    compressor_one = fields.Integer(required=True)
    compressor_two = fields.Integer(required=True)
    compressor_three = fields.Integer(required=True)
    compressor_four = fields.Integer(required=True)
    compressor_five = fields.Integer(required=True)
    created_on = fields.DateTime(required=True)


class ElectricityCreateResponseSchema(BaseEnergyCreateResponseSchema):
    total_kwh = fields.Integer(required=True)
    kilns = fields.Integer(required=True)
    shuttle_kilns = fields.Integer(required=True)


class NaturalGasCreateResponseSchema(BaseEnergyCreateResponseSchema):
    total_Nm3 = fields.Integer(required=True)
    kilns = fields.Integer(required=True)
    shuttle_kilns = fields.Integer(required=True)


class WaterCreateResponseSchema(BaseEnergyCreateResponseSchema):
    total_m3 = fields.Integer(required=True)
