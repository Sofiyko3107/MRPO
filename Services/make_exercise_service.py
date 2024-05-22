import datetime

from ..Model import Exercise


class MakeExerciseService:

    def _make_exercise(self, exercise: Exercise) -> Exercise:
        if ((len(exercise.emotions) >= 1 and len(exercise.events) >= 1) and
                (exercise.date < (datetime.datetime.now() + datetime.timedelta(days=1)))):
            return exercise
        else:
            return False

    def execute(self, exercise: Exercise) -> Exercise:
        return self._make_exercise(exercise)
