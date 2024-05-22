from ..Model import User


class UserServiceRegister:

    def _check_password(self, user: User) -> bool:
        if user.password > 8:
            return True
        else:
            return False

    def execute(self, user: User) -> User:
        return self._check_password(user)
