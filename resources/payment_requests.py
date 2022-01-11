from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.payment_requests import PaymentRequestsManager
from models import RoleType
from schemas.request.payment_requests import PaymentRequestsCreateRequestSchema
from schemas.response.payment_requests import PaymentRequestsCreateResponseSchema
from utils.decorator import permission_required, validate_schema


class ListUpdatePaymentRequestsTable(Resource):
    @auth.login_required()
    def get(self):
        id_ = auth.current_user()
        payment_requests = PaymentRequestsManager.get_all(id_.pk)
        schema = PaymentRequestsCreateResponseSchema()
        return schema.dump(payment_requests, many=True)

    @auth.login_required()
    @permission_required(RoleType.bulgargaz, RoleType.energo_pro)
    @validate_schema(PaymentRequestsCreateRequestSchema)
    def post(self):
        current_user = auth.current_user()
        payment_request = PaymentRequestsManager.create(
            request.get_json(), current_user
        )
        schema = PaymentRequestsCreateResponseSchema()
        return schema.dump(payment_request), 201


class PaymentRequestsDeleteAndUpdate(Resource):
    @auth.login_required()
    @permission_required(RoleType.bulgargaz, RoleType.energo_pro)
    def delete(self, id_):
        PaymentRequestsManager.delete(id_)
        return {"message": "Success"}, 204

    @auth.login_required()
    @permission_required(RoleType.bulgargaz, RoleType.energo_pro)
    @validate_schema(PaymentRequestsCreateRequestSchema)
    def put(self, id_):
        current_user = auth.current_user()
        update_data = PaymentRequestsManager.update(request.get_json(), id_, current_user.pk)
        schema = PaymentRequestsCreateResponseSchema()
        return schema.dump(update_data)


class ApprovePaymentRequest(Resource):
    @auth.login_required()
    @permission_required(RoleType.accountant)
    def get(self, id_):
        payment_request = PaymentRequestsManager.approve(id_)
        schema = PaymentRequestsCreateResponseSchema()
        return schema.dump(payment_request)


class RejectPaymentRequest(Resource):
    @auth.login_required()
    @permission_required(RoleType.accountant)
    def get(self, id_):
        payment_request = PaymentRequestsManager.reject(id_)
        schema = PaymentRequestsCreateResponseSchema()
        return schema.dump(payment_request)
