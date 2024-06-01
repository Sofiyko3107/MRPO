from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String)
    gender = Column(String)
    password = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'login': self.login,
            'gender': self.gender,
            'password': self.password  # Обратите внимание, что хранение паролей в открытом виде не рекомендуется!
        }


class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String)
    name = Column(String)
    DiaryMoods_id = Column(Integer, ForeignKey('diary_moods.id'))


class DiaryMoods(Base):
    __tablename__ = 'diary_moods'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))



class Achievement(Base):
    __tablename__ = 'achievements'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String)
    description = Column(String)
    diarymoods_id = Column(Integer, ForeignKey('diary_moods.id'))

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    influence = Column(String)
    exercise_id = Column(Integer, ForeignKey('exercises.id'))

class Emotion(Base):
    __tablename__ = 'emotions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    emotion_type = Column(String)
    intensity = Column(Integer)
    exercise_id = Column(Integer, ForeignKey('exercises.id'))


# Database setup
engine = create_engine('sqlite:///emotionDiary.db')
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()
