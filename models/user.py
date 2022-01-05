from db import db
from models.enums import RoleType


class BaseUserModel(db.Model):
    __abstract__ = True
    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


class PaymentReceiver(BaseUserModel):
    __tablename__ = "payment_receivers"

    iban = db.Column(db.String(22), nullable=False)
    role = db.Column(db.Enum(RoleType), default=RoleType.unknown, nullable=False)


class UserModel(BaseUserModel):
    __tablename__ = "users"
    role = db.Column(db.Enum(RoleType), default=RoleType.unknown, nullable=False)
