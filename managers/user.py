from psycopg2.errorcodes import UNIQUE_VIOLATION
from werkzeug.exceptions import BadRequest, InternalServerError, NotFound
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models.user import UserModel


class UserManager:
    @staticmethod
    def register(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = UserModel(**user_data)
        db.session.add(user)
        try:
            db.session.flush()
        except Exception as ex:
            if ex.origin.pgcode == UNIQUE_VIOLATION:
                raise BadRequest("Please login")
            else:
                InternalServerError("Server is unavailable. Please try again later")
        return user

    @staticmethod
    def login(user_data):
        user = UserModel.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("Not a valid email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Not a valid email or password")
        return user

    @staticmethod
    def update(user_role, id_):
        """
        Changes the users role to another.
        """
        user_q = UserModel.query.filter_by(pk=id_)
        user = user_q.first()

        if not user:
            raise NotFound("User not found")

        user_q.update(user_role)
        db.session.add(user)
        db.session.flush()
        return user
