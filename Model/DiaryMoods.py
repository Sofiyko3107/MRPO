from dataclasses import dataclass, field
from Model.User import User
from Model.Exercise import Exercise
from Model.Achievement import Achievement


@dataclass
class DiaryMoods:

    id: int
    user: User
    exercises: list[Exercise] = field(default_factory=list)
    achievements: list[Achievement] = field(default_factory=list)
    advices: list['Advice'] = field(default_factory=list)

    def __eq__(self, other):
        return self.id == other.id and self.user == other.user
