from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.energy import WaterManager, GasManager, ElectricityManager
from models import RoleType
from schemas.request.energy import WaterCreateRequestSchema, NaturalGasCreateRequestSchema, \
    ElectricityCreateRequestSchema, CompressorsCreateRequestSchema
from schemas.response.energy import WaterCreateResponseSchema, NaturalGasCreateResponseSchema, \
    ElectricityCreateResponseSchema, CompressorsCreateResponseSchema
from utils.decorator import validate_schema, permission_required, multiple_permissions_required


class ListUpdateWaterTable(Resource):

    @auth.login_required()
    def get(self):
        water_amount = WaterManager.get_all()
        schema = WaterCreateResponseSchema()
        return schema.dump(water_amount, many=True)

    @auth.login_required()
    @permission_required(RoleType.data_entry)
    @validate_schema(WaterCreateRequestSchema)
    def post(self):
        current_user = auth.current_user()
        energy = WaterManager.create(request.get_json(), current_user.pk)
        schema = WaterCreateRequestSchema()
        return schema.dump(energy)


class WaterDataDeleteAndUpdate(Resource):
    @auth.login_required()
    @permission_required(RoleType.data_entry)
    def delete(self, id_):
        WaterManager.delete(id_)
        return {'message': 'Success'}, 204

    @auth.login_required()
    @multiple_permissions_required(RoleType.data_entry, RoleType.data_analyst)
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
    @permission_required(RoleType.data_entry)
    @validate_schema(NaturalGasCreateRequestSchema)
    def post(self):
        current_user = auth.current_user()
        energy = GasManager.create(request.get_json(), current_user.pk)
        schema = NaturalGasCreateRequestSchema()
        return schema.dump(energy)


class GasDataDeleteAndUpdate(Resource):
    @auth.login_required()
    @permission_required(RoleType.data_entry)
    def delete(self, id_):
        GasManager.delete(id_)
        return {"message" : "Success"}, 204

    @auth.login_required()
    @multiple_permissions_required(RoleType.data_entry, RoleType.data_analyst)
    @validate_schema(NaturalGasCreateRequestSchema)
    def put(self, id_):
        update_data = GasManager.update(request.get_json(), id_)
        schema = NaturalGasCreateRequestSchema()
        return schema.dump(update_data)


class ListUpdateElectricityTable(Resource):

    @auth.login_required()
    def get(self):
        electricity_amount = ElectricityManager.get_all()
        schema = ElectricityCreateResponseSchema()
        return schema.dump(electricity_amount, many=True)

    @auth.login_required()
    @permission_required(RoleType.data_entry)
    @validate_schema(ElectricityCreateRequestSchema)
    def post(self):
        current_user = auth.current_user()
        energy = ElectricityManager.create(request.get_json(), current_user.pk)
        schema = ElectricityCreateRequestSchema()
        return schema.dump(energy)


class ElectricityDeleteAndUpdate(Resource):
    @auth.login_required()
    @permission_required(RoleType.data_entry)
    def delete(self, id_):
        ElectricityManager.delete(id_)
        return {'message':'Success'}, 204

    @auth.login_required()
    @multiple_permissions_required(RoleType.data_entry, RoleType.data_analyst)
    @validate_schema(ElectricityCreateRequestSchema)
    def put(self, id_):
        update_data = ElectricityManager.update(request.get_json(), id_)
        schema = ElectricityCreateRequestSchema()
        return schema.dump(update_data)

class ListUpdateCompressorsTable(Resource):

    @auth.login_required()
    def get(self):
        compressors_amount = CompressorsManager.get_all()
        schema = CompressorsCreateResponseSchema()
        return schema.dump(compressors_amount, many=True)

    @auth.login_required()
    @permission_required(RoleType.data_entry)
    @validate_schema(CompressorsCreateRequestSchema)
    def post(self):
        current_user = auth.current_user()
        energy = CompressorsManager.create(request.get_json(), current_user.pk)
        schema = CompressorsCreateRequestSchema()
        return schema.dump(energy)

class CompressorsDeleteAndUpdate(Resource):
    @auth.login_required()
    @permission_required(RoleType.data_entry)
    def delete(self, id_):
        CompressorsManager.delete(id_)
        return {'message' : 'Success'}, 204

    @auth.login_required()
    @multiple_permissions_required(RoleType.data_entry, RoleType.data_analyst)
    @validate_schema(CompressorsCreateRequestSchema)
    def put(self, id_):
        update_data = CompressorsManager.update(request.get_json(), id_)
        schema = CompressorsCreateRequestSchema()
        return schema.dump(update_data)
