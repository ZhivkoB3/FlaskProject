from flask import request
from flask_restful import Resource

from managers.auth import AuthManager
from managers.user import UserManager, ServiceProvidersManager
from schemas.request.user import (
    BaseUserSchema,
    BaseUserRegisterSchema,
    PaymentReceiverRegisterSchema,
)
from utils.decorator import validate_schema


class Register(Resource):
    @validate_schema(BaseUserRegisterSchema)
    def post(self):
        user = UserManager.register(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 201


class ServiceProvider(Resource):
    @validate_schema(PaymentReceiverRegisterSchema)
    def post(self):
        user = ServiceProvidersManager.register(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 201


class Login(Resource):
    @validate_schema(BaseUserSchema)
    def post(self):
        user = UserManager.login(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 200


class LoginServiceProvider(Resource):
    @validate_schema(BaseUserSchema)
    def post(self):
        user = ServiceProvidersManager.login(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 200
