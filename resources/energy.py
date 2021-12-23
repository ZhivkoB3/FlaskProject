from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.energy import WaterManager, GasManager
from schemas.request.energy import WaterCreateRequestSchema, NaturalGasCreateRequestSchema
from schemas.response.energy import WaterCreateResponseSchema, NaturalGasCreateResponseSchema
from utils.decorator import validate_schema


class ListUpdateWaterTable(Resource):

    @auth.login_required()
    def get(self):
        water_amount = WaterManager.get_all()
        schema = WaterCreateResponseSchema()
        return schema.dump(water_amount, many=True)

    @auth.login_required()
    @validate_schema(WaterCreateRequestSchema)
    def post(self):
        current_user = auth.current_user()
        energy = WaterManager.create(request.get_json(), current_user.pk)
        schema = WaterCreateRequestSchema()
        return schema.dump(energy)


class WaterDataDeleteAndUpdate(Resource):
    @auth.login_required()
    def delete(self, id_):
        WaterManager.delete(id_)
        return {'message': 'Success'}, 204

    @auth.login_required()
    @validate_schema(WaterCreateRequestSchema)
    def put(self, id_):
        update_data = WaterManager.update(request.get_json(), id_)
        schema = WaterCreateRequestSchema()
        return schema.dump(update_data)


class ListUpdateGasTable(Resource):

    @auth.login_required()
    def get(self):
        gas_amount = GasManager.get_all()
        schema = NaturalGasCreateResponseSchema()
        return schema.dump(gas_amount, many=True)

    @auth.login_required()
    @validate_schema(NaturalGasCreateRequestSchema)
    def post(self):
        current_user = auth.current_user()
        energy = GasManager.create(request.get_json(), current_user.pk)
        schema = NaturalGasCreateRequestSchema()
        return schema.dump(energy)