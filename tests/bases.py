from flask_testing import TestCase

from config import create_app
from db import db
from tests.factories import AccountantFactory
from tests.helpers import generate_token


class BaseTestCase(TestCase):
    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_app(self):
        self.headers = {"Content-Type": "application/json"}
        return create_app("config.TestApplicationConfig")


