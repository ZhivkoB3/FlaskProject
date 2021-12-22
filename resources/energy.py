from flask import request
from flask_restful import Resource

# from managers.energy import EnergyManager
from models.energy import WaterModel
# from schemas.response.energy import EnergyCreateResponseSchema


# class RequestPayment(Resource):
#     def post(self):
#         current_user = auth.current_user()
#         # invoice =



# class UploadData(Resource):
#     def post(self):
#         energy = EnergyManager.create(request.get_json())
#         schema = EnergyCreateResponseSchema()
#         return schema.dump(energy)