
class Achievement:
    def __init__(self, id, date, description):
        self.id = id
        self.date = date
        self.description = description

    def get_info(self):
        return [self.id, self.date, self.description]