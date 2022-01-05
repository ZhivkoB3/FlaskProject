from managers.auth import auth
from managers.user import UserManager
from flask import request

from models import RoleType
from schemas.response.user import BaseUserResponseSchema
from flask_restful import Resource

from utils.decorator import permission_required


class ChangeUserRole(Resource):
    @auth.login_required
    @permission_required(RoleType.ceo)
    def put(self, id_):
        update_data = UserManager.update(request.get_json(), id_)
        schema = BaseUserResponseSchema()
        return {'message': 'Role changed!'}, 200