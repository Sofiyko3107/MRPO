class Achievement:
    def __init__(self, date, description):
        self.date = date
        self.description = description

    def get_info(self):
        return [self.date, self.description]