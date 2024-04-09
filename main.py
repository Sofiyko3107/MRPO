import datetime

from faker import Faker
from Model.Achievement import Achievement
from Model.Emotion import Emotion
from Model.DiaryMoods import DiaryMoods
from Model.Event import Event
from Model.User import User
from Model.Exercise import Exercise
from Repository.UserRepository import UserRepository
from Repository.AchievementRepository import AchievementRepository
from Repository.DiaryMoodRepository import DiaryMoodRepository
from Repository.EmotionRepository import EmotionRepository
from Repository.EventRepository import EventRepository
from Repository.ExerciseRepository import ExerciseRepository

# 1)Только зарегистрированный пользователь может вести дневник
# 2)Задание должно содержать хотябы одну эмоцию и одно событие
# 3)Дата задания не должна быть больше сегоднешнего дня
# 4)Пользователь может зарегистрироваться, если длина его пароля >=8

fake = Faker()

emotion_repository = EmotionRepository()
event_repository = EventRepository()
exercise_repository = ExerciseRepository()
achievement_repository = AchievementRepository()
user_repository = UserRepository()
diary_repository = DiaryMoodRepository()

em1 = Emotion(1, 'Радость', 10)
em2 = Emotion(2, 'Грусть', 10)
em3 = Emotion(3, 'Страх', 3)

ev1 = Event(1, "Плохая оценка", "Грусть")
ev2 = Event(2, "Вкусно покушала", "Радость")
ev3 = Event(3, "Подарили цветочки", "Любовь")
ev4 = Event(4, "Не встретили с вокзала", "Обида")

ex1 = Exercise(1, datetime.datetime(2024, 3, 8), [ev2, ev3], [em1])
ex2 = Exercise(2, datetime.datetime(2024, 2, 23), [ev2], [em1])
ex3 = Exercise(3, datetime.datetime(2024, 2, 20), [ev4], [em2, em3])
ex4 = Exercise(4, datetime.datetime(2024, 3, 8), [], [em1])
ex5 = Exercise(5, datetime.datetime(2024, 5, 26), [ev1], [em1])

a1 = Achievement(1, datetime.datetime(2003, 11, 28), 'Главное достижение')
a2 = Achievement(2, datetime.datetime(2021, 6, 16), 'Сдал ЕГЭ по математике')
a3 = Achievement(3, datetime.datetime(2021, 5, 28), 'Сдал ЕГЭ по русскому')

U1 = User(id=1, login=f"{fake.word()}", gender='male', password="123456789")
U2 = User(id=2, login=f"{fake.word()}", gender='female', password="987654321")
U3 = User(id=3, login=f"{fake.word()}", gender='female', password="123444")

d1 = DiaryMoods(1, U1, [ex1, ex2], [a2, a3], ['Никогда не сдавайся'])
d2 = DiaryMoods(2, U2, [ex3], [a1], ['Не будь лапшой'])
d3 = DiaryMoods(3, U3, [ex2], [a3], ['Just do it!!!'])

emotion_repository.add(em1)
emotion_repository.add(em2)
emotion_repository.add(em3)

event_repository.add(ev1)
event_repository.add(ev2)
event_repository.add(ev3)
event_repository.add(ev4)

achievement_repository.add(a1)
achievement_repository.add(a2)
achievement_repository.add(a3)


def auth(user_id):
    if user_repository.get_by_id(user_id):
        return True
    else:
        return False


def register(user: User):
    if len(user.password) >= 8 and auth(user.id):
        user_repository.add(user)
        return True
    else:
        return False


def make_exercise(exercise: Exercise):
    if (len(exercise.emotions) >= 1 and len(exercise.events) >= 1) and (exercise.date < (datetime.datetime.now() + datetime.timedelta(days=1))):
        exercise_repository.add(exercise)
        return True
    else:
        return False


def make_diary(diarymood: DiaryMoods):
    if auth(diarymood.user.id):
        diary_repository.add(diarymood)
        return True
    else:
        return False


register(U1)
register(U2)
register(U3)

make_exercise(ex1)
make_exercise(ex2)
make_exercise(ex3)
make_exercise(ex4)
make_exercise(ex5)

make_diary(d1)
make_diary(d2)
make_diary(d3)
