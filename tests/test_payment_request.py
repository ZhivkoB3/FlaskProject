import json
from unittest.mock import patch

from managers.payment_requests import PaymentRequestsManager
from models import PaymentRequestsModel, State
from tests.bases import BaseTestCase
from tests.factories import PaymentReceiverFactory, AccountantFactory
from tests.helpers import mock_uuid, generate_token, object_as_dict


class TestPaymentRequest(BaseTestCase):
    @patch("uuid.uuid4", mock_uuid)
    @patch.object(PaymentRequestsManager, "issue_transaction", return_value=None)
    def test_create_payment_request(self, wise_mock_issue):
        url = "/payments"
        data = {
            "amount": 999,
            "metric": "kwh",
            "type": "gaz",
            "total_invoice_amount": 9999,
        }

        payment_receiver = PaymentReceiverFactory()
        token = generate_token(payment_receiver)
        self.headers.update({"Authorization": f"Bearer {token}"})
        payment_request = PaymentRequestsModel.query.all()
        assert len(payment_request) == 0

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        payment_request = PaymentRequestsModel.query.all()
        assert len(payment_request) == 1

        created_payment_request = object_as_dict(payment_request[0])
        created_payment_request.pop("created_on")

        assert created_payment_request == {
            "pk": payment_request[0].pk,
            "user_id": payment_request[0].user_id,
            "state": State.pending,
            "updated_by": None,
            "updated_on": None,
            **data,
        }

        expected_resp = {
            "pk": payment_request[0].pk,
            "user_id": payment_request[0].user_id,
            "state": "State.pending",
            "updated_by": None,
            "updated_on": None,
            **data,
        }

        actual_resp = resp.json
        actual_resp.pop("created_on")
        assert resp.status_code == 201
        assert actual_resp == expected_resp

        wise_mock_issue.assert_called_once_with(
            data["total_invoice_amount"],
            f"{payment_receiver.first_name} " f"{payment_receiver.last_name}",
            payment_receiver.iban,
            payment_request[0].pk,
        )


class TestCancelPaymentRequest(BaseTestCase):
    @patch.object(PaymentRequestsManager, "reject", return_value=None)
    def test_create_payment_request(self, wise_mock_issue):
        url = "/accountants/payments/1/rejected"

        accountant = AccountantFactory()
        token = generate_token(accountant)
        self.headers.update({"Authorization": f"Bearer {token}"})

        self.client.get(url, headers=self.headers)

        wise_mock_issue.assert_called_once_with(1)


class TestApprovePaymentRequest(BaseTestCase):
    @patch.object(PaymentRequestsManager, "approve", return_value=None)
    def test_create_payment_request(self, wise_mock_issue):
        url = "/accountants/payments/1/approved"

        accountant = AccountantFactory()
        token = generate_token(accountant)
        self.headers.update({"Authorization": f"Bearer {token}"})

        self.client.get(url, headers=self.headers)

        wise_mock_issue.assert_called_once_with(1)



