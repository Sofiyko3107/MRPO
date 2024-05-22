from MRPO.Repository.AbstractRepository import AbstractRepository

class ExerciseRepository(AbstractRepository):

    def __init__(self):
        self.exercises = []

    def add(self, exercise):
        self.exercises.append(exercise)

    def remove(self, exercise):
        if self.exercises:
            for e in self.exercises:
                if e.login == exercise.login:
                    self.exercises.remove(e)

    def get_all(self):
        return self.exercises

    def get_by_id(self, id):
        if self.exercises:
            for e in self.exercises:
                if e.id == id:
                    return e
        return "Задания по данному id не найдено"
