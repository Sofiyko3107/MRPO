
class User:
    def __init__(self, login, gender,  password):
        self.login = login
        self.gender = gender
        self.password = password

    def get_info(self):
        return [self.login, self.gender, self.password]
