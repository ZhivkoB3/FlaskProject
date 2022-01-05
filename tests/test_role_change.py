import json

from models import UserModel
from tests.bases import BaseTestCase
from tests.factories import CEOFactory, UnknownFactory
from tests.helpers import generate_token, object_as_dict


class TestRoleChange(BaseTestCase):
    """
    Checks the database if users are present
    Add a user to the database using factory
    Check if the user has been added to the db
    Check if the user has been added correctly
    Changes the role of the user
    Returns 200 and returns a message.
    """
    def test_role_change(self):

        users = UserModel.query.all()
        assert len(users) == 0

        base_user = UnknownFactory()
        users = UserModel.query.all()
        assert len(users) == 1

        users_data_added = object_as_dict(users[0])

        assert users_data_added == {
            'pk': users[0].pk,
            'first_name': users[0].first_name,
            'last_name': users[0].last_name,
            'phone': users[0].phone,
            'email': users[0].email,
            'password': users[0].password,
            'role': users[0].role
        }

        url = '/role_change/1'

        data = {
            "role": "data_analyst"
        }

        ceo = CEOFactory()
        token = generate_token(ceo)
        self.headers.update({"Authorization": f"Bearer {token}"})
        resp = self.client.put(url, data=json.dumps(data), headers=self.headers)

        assert resp.status_code == 200
        assert resp.json == {'message': 'Role changed!'}
