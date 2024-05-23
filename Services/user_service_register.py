from flask import jsonify

from MRPO.UoW.UoW import SqlAlchemyUnitOfWork
from MRPO.DBModel import User


class UserServiceRegister:

    def __init__(self, uow: SqlAlchemyUnitOfWork):
        self.uow = uow

    def _check_password(self, user: User) -> bool:
        if len(user.password) > 8:
            return True
        else:
            return False

    def execute(self, data):
        with self.uow:
            user = User(
                login=data['login'],
                gender=data['gender'],
                password=data['password']
            )
            if self._check_password(user):
                self.uow.repository.add(user)
                self.uow.commit()
                return user.to_dict()
