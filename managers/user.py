from werkzeug.exceptions import BadRequest, InternalServerError
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from psycopg2.errorcodes import UNIQUE_VIOLATION
from models.user import DataEntry


class UserManager:
    @staticmethod
    def register(user_data, role):
        user_data['password'] = generate_password_hash(user_data['password'])
        user = role(**user_data)
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as ex:
            if ex.origin.pgcode == UNIQUE_VIOLATION:
                raise BadRequest('Please login')
            else:
                InternalServerError('Server is unavailable. Please try again later')
        return user

    @staticmethod
    def login(user_data):
        user = DataEntry.query.filter_by(email=user_data['email']).first()
        if not user:
            raise BadRequest('Not a valid email or password')

        if not check_password_hash(user.password, user_data['password']):
            raise BadRequest('Not a valid email or password')
        return user
