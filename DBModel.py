from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String)
    gender = Column(String)
    password = Column(String)

class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))


class DiaryMoods(Base):
    __tablename__ = 'diary_moods'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")
    exercise_id = Column(Integer, ForeignKey('exercises.id'))


class Achievement(Base):
    __tablename__ = 'achievements'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    description = Column(String)


class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    influence = Column(String)


class Emotion(Base):
    __tablename__ = 'emotions'
    id = Column(Integer, primary_key=True)
    emotion_type = Column(String)
    intensity = Column(Integer)


# Database setup
engine = create_engine('sqlite:///emotionDiary.db')
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()
