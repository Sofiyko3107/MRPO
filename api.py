from flask import Flask, jsonify, request, url_for, render_template
import requests
from MRPO.UoW.UoW import SqlAlchemyUnitOfWork
from MRPO.DBModel import User, DiaryMoods, Exercise
from MRPO.Services.user_service_register import UserServiceRegister


app = Flask(__name__, template_folder='template')


# Настройка подключения к базе данных


@app.route("/user/<int:user_id>")
def get_user(user_id):
    print(user_id)
    uow = SqlAlchemyUnitOfWork()
    with uow:
        user = uow.repository.get_by_id(User, user_id)

        if user is None:
            return dict()
        return user.to_dict()


@app.route("/user/add", methods=["POST"])
def add_user():
    uow = SqlAlchemyUnitOfWork()
    uservice = UserServiceRegister(uow)

    data = request.json
    user = uservice.execute(data)
    diary_moods = DiaryMoods(user_id=user['id'])
    uow.repository.add(diary_moods)
    uow.commit()
    return {'user': user}


@app.route("/user/form", methods=["GET", "POST"])
def user_form():
    if request.method == "POST":
        path = "http://localhost:5000" + url_for("add_user")
        response = requests.post(path, json=request.form)
        return render_template("input.html", response=response.json())
    else:
        return render_template("input.html")

@app.route("/exercise/add", methods=["POST"])
def add_exercise():
    uow = SqlAlchemyUnitOfWork()
    data = request.json
    print(data)
    with uow:
        diaries = uow.repository.get_all(DiaryMoods)
        print('im here', data['user'])
        for diary in diaries:

            if int(diary.user_id) == int(data['user']):
                diary_mood_id = diary.id
        exercise = Exercise(date=data["date"], name=data["exercise"],  DiaryMoods_id= diary_mood_id )
        uow.repository.add(exercise)
        uow.commit()
    return {}



@app.route("/exercise/form", methods=["GET", "POST"])
def exercise_form():
    uow = SqlAlchemyUnitOfWork()

    users_form = []
    with uow:
        users = uow.repository.get_all(User)
        for u in users:
            users_form.append(u.to_dict())

    if request.method == "POST":
        path = "http://localhost:5000" + url_for("add_exercise")
        response = requests.post(path, json=request.form)
        return render_template("exercise.html", response=response.json(), users_form=users_form)
    else:
        return render_template("exercise.html", users_form=users_form)


if __name__ == '__main__':
    app.run(debug=True)
