import json

from flask_testing import TestCase

from config import create_app
from db import db
from models import UserModel, RoleType
from tests.bases import BaseTestCase

from tests.helpers import object_as_dict


class TestAuth(BaseTestCase):
    """
    Check if a user can be registered correctly.
    """
    def test_register_user(self):
        url = '/register'

        data = {
            'password': 'asddsa',
            'first_name': 'Some first name',
            'last_name': 'Some last name',
            'phone': '0898123456113',
            'email': 'abc@cba.com'
        }

        users = UserModel.query.all()
        assert len(users) == 0

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        assert resp.status_code == 201
        assert 'token' in resp.json
        users = UserModel.query.all()
        assert len(users) == 1
        user = object_as_dict(users[0])
        user.pop('password')
        data.pop('password')

        assert user == {
            'pk': user['pk'],
            'role': RoleType.unknown,
            **data
        }