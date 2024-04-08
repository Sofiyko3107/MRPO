from dataclasses import dataclass


@dataclass
class User:
    id: int
    login: str
    gender: str
    password: str

    def __eq__(self, other):
        return self.id == other.id and self.login == other.login
