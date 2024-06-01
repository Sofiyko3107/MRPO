from dataclasses import dataclass, field
from Model.User import User
from Model.Exercise import Exercise
from Model.Achievement import Achievement

@dataclass
@dataclass
class DiaryMoods:

    def __init__(self, id: int, user: User, exercises: list[Exercise], achievements: list[Achievement],
                 advices: list['']):
        self.id = id
        self.user = user
        self.exercises = exercises
        self.achievements = achievements
        self.advices = advices

    def __eq__(self, other):
        return self.id == other.id and self.user == other.user
