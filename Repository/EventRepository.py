from Repository import FakeRepository


class EventRepository(FakeRepository.FakeRepository):

    def __init__(self):
        self.events = []

    def add(self, event):
        self.events.append(event)

    def remove(self, event):
        if self.events:
            for e in self.events:
                if e.login == event.login:
                    self.events.remove(e)

    def get_all(self):
        return self.events

    def get_by_id(self, id):
        if self.events:
            for e in self.events:
                if e.id == id:
                    return e
        return "События по данному id не найдено"