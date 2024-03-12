
class DiaryMoods:
    def __init__(self, id, user, exercises, achievements, advices):
        self.id = id
        self.user = user
        self.exercises = exercises
        self.achievements = achievements
        self.advices = advices

    def get_info(self):
        user = self.user.get_info()
        exercises = []
        achievements = []

        if self.exercises:
            for e in self.exercises:
                exercises.append(e.get_info())

        if self.achievements:
            for a in self.achievements:
                achievements.append(a.get_info())

        data = {'id' : id, 'user': user, 'exercises': exercises, 'achievements': achievements, 'advices': self.advices}

        return data
