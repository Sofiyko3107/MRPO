from dataclasses import dataclass


class User:

    def __init__(self, id: int, login: str, gender: str, password: str):
        self.id = id
        self.login = login
        self.gender = gender
        self.password = password

    def __eq__(self, other):
        return self.id == other.id and self.login == other.login
