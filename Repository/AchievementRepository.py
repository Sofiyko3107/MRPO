from MRPO.Repository.AbstractRepository import AbstractRepository


class AchievementRepository(AbstractRepository):

    def __init__(self):
        self.achievements = []

    def add(self, achievement):
        self.achievements.append(achievement)

    def remove(self, achievement):
        if self.achievements:
            for a in self.achievements:
                if a.id == achievement.id:
                    self.achievements.remove(a)

    def get_all(self):
        return self.achievements

    def get_by_id(self, id):
        if self.achievements:
            for a in self.achievements:
                if a.id == id:
                    return a
        return "Достижений по данному id не найден"
