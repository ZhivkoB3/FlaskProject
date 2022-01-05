import json

from models import UserModel
from tests.bases import BaseTestCase
from tests.factories import AccountantFactory, DataEntryFactory, DataAnalystFactory, UnknownFactory
from tests.helpers import generate_token, object_as_dict


class TestRoleChangeUnknown(BaseTestCase):
    """
    Checks the database if users are present
    Add a user to the database using factory
    Check if the user has been added to the db
    Check if the user has been added correctly
    Tries to change the role of the user
    Raises 403 and return a message because
    this user does not have a permission.
    """
    def test_role_change_with_unknown(self):

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

        url = f'/role_change/{users[0].pk}'

        data = {
            "role": "data_analyst"
        }

        unknown_user = UnknownFactory()
        token = generate_token(unknown_user)
        self.headers.update({"Authorization": f"Bearer {token}"})
        resp = self.client.put(url, data=json.dumps(data), headers=self.headers)

        assert resp.status_code == 403
        assert resp.json == {"message": "You do not have access to this resource"}


class TestRoleChangeDataAnalyst(BaseTestCase):
    """
    Check TestRoleChangeUnknown comment
    """
    def test_role_change_with_data_analyst(self):

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

        url = f'/role_change/{users[0].pk}'

        data = {
            "role": "data_analyst"
        }
        data_analyst = DataAnalystFactory()
        token = generate_token(data_analyst)
        self.headers.update({"Authorization": f"Bearer {token}"})
        resp = self.client.put(url, data=json.dumps(data), headers=self.headers)

        assert resp.status_code == 403
        assert resp.json == {"message": "You do not have access to this resource"}


class TestRoleChangeDataEntry(BaseTestCase):
    """
    Check TestRoleChangeUnknown comment
    """
    def test_role_change_with_data_entry(self):

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

        data_entry = DataEntryFactory()
        token = generate_token(data_entry)
        self.headers.update({"Authorization": f"Bearer {token}"})
        resp = self.client.put(url, data=json.dumps(data), headers=self.headers)

        assert resp.status_code == 403
        assert resp.json == {"message": "You do not have access to this resource"}


class TestRoleChangeAccountant(BaseTestCase):
    """
    Check TestRoleChangeUnknown comment
    """
    def test_role_change_with_accountant(self):

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

        accountant = AccountantFactory()
        token = generate_token(accountant)
        self.headers.update({"Authorization": f"Bearer {token}"})
        resp = self.client.put(url, data=json.dumps(data), headers=self.headers)

        assert resp.status_code == 403
        assert resp.json == {"message": "You do not have access to this resource"}