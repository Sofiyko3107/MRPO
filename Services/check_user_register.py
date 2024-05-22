from ..Model import User
from ..Repository import UserRepository


class CheckUserRegister():
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def _check_user_register(self, user: User) -> bool:
        if self.user_repository.get_by_id(user.id):
            return True
        else:
            return False

    def execute(self, user: User) -> bool:
        return self._check_user_register(user)
