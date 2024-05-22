from MRPO.Repository.AbstractRepository import AbstractRepository

class DiaryMoodRepository(AbstractRepository):

    def __init__(self):
        self.diaryMoods = []

    def add(self, diaryMood):
        self.diaryMoods.append(diaryMood)

    def remove(self, diaryMood):
        if self.diaryMoods:
            for d in self.diaryMoods:
                if d.id == diaryMood.login:
                    self.diaryMoods.remove(d)

    def get_all(self):
        return self.diaryMoods

    def get_by_id(self, id):
        if self.diaryMoods:
            for d in self.diaryMoods:
                if d.id == id:
                    return d
        return "Запись по данному id не найдена"