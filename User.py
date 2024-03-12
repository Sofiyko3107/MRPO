
class User:
    def __init__(self, id, login, gender,  password):
        self.id = id
        self.login = login
        self.gender = gender
        self.password = password

    def get_info(self):
        return [self.id, self.login, self.gender, self.password]
