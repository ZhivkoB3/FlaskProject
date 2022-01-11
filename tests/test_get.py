from tests.bases import BaseTestCase
from tests.factories import AccountantFactory
from tests.helpers import generate_token


class TestGetWater(BaseTestCase):
    def test_get_water(self):
        url = "/energy/water"

        accountant = AccountantFactory()
        token = generate_token(accountant)
        self.headers.update({"Authorization": f"Bearer {token}"})

        self.client.get(url, headers=self.headers)


class TestGetGas(BaseTestCase):
    def test_get_gas(self):
        url = "/energy/gas"
        accountant = AccountantFactory()
        token = generate_token(accountant)
        self.headers.update({"Authorization": f"Bearer {token}"})

        self.client.get(url, headers=self.headers)


class TestGetElElectricity(BaseTestCase):
    def test_get_electricity(self):
        url = "/energy/electricity"

        accountant = AccountantFactory()
        token = generate_token(accountant)
        self.headers.update({"Authorization": f"Bearer {token}"})

        self.client.get(url, headers=self.headers)


class TestGetCompressors(BaseTestCase):
    def test_get_compressors(self):
        url = "/energy/compressors"

        accountant = AccountantFactory()
        token = generate_token(accountant)
        self.headers.update({"Authorization": f"Bearer {token}"})

        self.client.get(url, headers=self.headers)


class TestGetPaymentRequest(BaseTestCase):
    def test_get_payment_request(self):
        url = "/payments"

        accountant = AccountantFactory()
        token = generate_token(accountant)
        self.headers.update({"Authorization": f"Bearer {token}"})

        self.client.get(url, headers=self.headers)
