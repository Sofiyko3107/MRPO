class Event:
    def __init__(self, description, influence):
        self.description = description
        self.influence = influence

    def get_info(self):
        return [self.description, self.influence]