from faker import Faker
import Event as ev
import Emotion as em
import Exercise as ex
import DiaryMoods as d
import Achievement as a
import User as u
from Repository import UserRepository as uR

fake = Faker()

em1 = em.Emotion('Радость', 10)
em2 = em.Emotion('Грусть', 10)
em3 = em.Emotion('Страх', 3)

ev1 = ev.Event("Плохая оценка", "Грусть")
ev2 = ev.Event("Вкусно покушала", "Радость")
ev3 = ev.Event("Подарили цветочки", "Любовь")
ev4 = ev.Event("Не встретили с вокзала", "Обида")

ex1 = ex.Exercise('08.03.24', [ev2, ev3], [em1])
ex2 = ex.Exercise('23.02.24', [ev2], [em1])
ex3 = ex.Exercise('20.02.24', [ev4], [em2, em3])

a1 = a.Achievement('28.11.2003', 'Главное достижение')
a2 = a.Achievement('16.06.2021', 'Сдал ЕГЭ по математике')
a3 = a.Achievement('28.05.2021', 'Сдал ЕГЭ по русскому')

U1 = u.User(id=1, login=f"{fake.word()}", gender='male', password="123")
U2 = u.User(id=2, login=f"{fake.word()}", gender='female', password="123")
U3 = u.User(id=3, login=f"{fake.word()}", gender='female', password="123")

d1 = d.DiaryMoods(U1, [ex1, ex2], [a2, a3], 'Никогда не сдавайся')
d2 = d.DiaryMoods(U2, [ex3], [a1], 'Не будь лапшой')

uRep = uR.UserRepository()

uRep.add(U1)
uRep.add(U2)
uRep.add(U3)

print(uRep.get_all())

uRep.remove(U3)
print(uRep.get_by_id(2))

print(uRep.get_by_id(5))

print(d1.get_info())
print(d2.get_info())


