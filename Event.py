
class Event:
    def __init__(self, id, description, influence):
        self.id = id
        self.description = description
        self.influence = influence

    def get_info(self):
        return [self.id, self.description, self.influence]