import uuid

from werkzeug.exceptions import NotFound

from db import db
from models import PaymentRequestsModel, State, TransactionModel
from services.wise import WiseService

wise = WiseService()


class PaymentRequestsManager:
    @staticmethod
    def get_all(id_):
        return PaymentRequestsModel.query.filter_by(user_id=id_)

    @staticmethod
    def issue_transaction(amount, full_name, iban, payment_request_id):
        quote_id = wise.create_quote(amount)
        recipient_id = wise.create_recipient(full_name, iban)
        custom_id = str(uuid.uuid4())
        transfer_id = wise.create_transfer(recipient_id, quote_id, custom_id)
        transfer_data = {
            "quote_id": quote_id,
            "transfer_id": transfer_id,
            "target_account_id": custom_id,
            "amount": amount,
            "payment_request_id": payment_request_id,
        }
        transfer = TransactionModel(**transfer_data)
        db.session.add(transfer)
        db.session.flush()

    @staticmethod
    def create(data, payment_receiver):
        data["user_id"] = payment_receiver.pk
        amount = data["total_invoice_amount"]
        full_name = f"{payment_receiver.first_name} {payment_receiver.last_name}"
        iban = payment_receiver.iban
        payment_data = PaymentRequestsModel(**data)
        db.session.add(payment_data)
        db.session.flush()
        PaymentRequestsManager.issue_transaction(
            amount, full_name, iban, payment_data.pk
        )
        return payment_data

    @staticmethod
    def delete(id_):
        payment_data_q = PaymentRequestsModel.query.filter_by(pk=id_)
        payment_data = payment_data_q.first()

        if not payment_data:
            raise NotFound("Data not present")

        db.session.delete(payment_data)
        db.session.flush()

    @staticmethod
    def update(data, id_, payment_receiver):
        data["updated_by"] = payment_receiver
        payment_data_q = PaymentRequestsModel.query.filter_by(pk=id_)
        payment_data = payment_data_q.first()

        if not payment_data:
            raise NotFound("Data not present")

        payment_data_q.update(data)
        db.session.add(payment_data)
        db.session.flush()
        return payment_data

    @staticmethod
    def approve(id_):
        payment_request_q = PaymentRequestsModel.query.filter_by(pk=id_)
        payment_request = payment_request_q.first()
        if not payment_request:
            raise NotFound("This payment request does not exist")
        transfer = TransactionModel.query.filter_by(payment_request_id=id_).first()
        wise.fund_transfer(transfer.transfer_id)
        payment_request_q.update({"state": State.approved})
        db.session.add(payment_request)
        db.session.flush()
        return payment_request

    @staticmethod
    def reject(id_):
        payment_request_q = PaymentRequestsModel.query.filter_by(pk=id_)
        payment_request = payment_request_q.first()
        if not payment_request:
            raise NotFound("This payment request does not exist")
        transfer = TransactionModel.query.filter_by(payment_request_id=id_).first()
        wise.cancel_transfer(transfer.transfer_id)
        payment_request_q.update({"state": State.rejected})
        db.session.add(payment_request)
        db.session.flush()
        return payment_request
