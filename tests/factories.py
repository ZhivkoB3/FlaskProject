from random import randint

import factory

from db import db
from models import UserModel, RoleType, PaymentReceiverModel, TransactionModel
from tests.helpers import mock_uuid


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        obj = super().create(**kwargs)
        db.session.add(obj)
        db.session.flush()
        return obj


class BaseUser(BaseFactory):
    class Meta:
        model = UserModel

    pk = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    phone = str(randint(100000, 300000))
    email = factory.Faker("email")
    password = factory.Faker("password")


class UnknownFactory(BaseUser):
    role = RoleType.unknown


class DataEntryFactory(BaseUser):
    role = RoleType.data_entry


class DataAnalystFactory(BaseUser):
    role = RoleType.data_analyst


class AccountantFactory(BaseUser):
    role = RoleType.accountant


class CEOFactory(BaseUser):
    role = RoleType.ceo


class PaymentReceiverFactory(BaseFactory):
    class Meta:
        model = PaymentReceiverModel

    pk = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    phone = str(randint(100000, 300000))
    email = factory.Faker("email")
    password = factory.Faker("password")
    role = RoleType.bulgargaz
    iban = factory.Faker("iban")
