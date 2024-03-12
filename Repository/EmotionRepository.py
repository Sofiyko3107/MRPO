from Repository import FakeRepository


class EmotionRepository(FakeRepository.FakeRepository):

    def __init__(self):
        self.emotions = []

    def add(self, emotion):
        self.emotions.append(emotion)

    def remove(self, emotion):
        if self.emotions:
            for e in self.emotions:
                if e.login == emotion.login:
                    self.emotions.remove(e)

    def get_all(self):
        return self.emotions

    def get_by_id(self, id):
        if self.emotions:
            for e in self.emotions:
                if e.id == id:
                    return e
        return "Эмоциональное состояние по данному id не найдено"