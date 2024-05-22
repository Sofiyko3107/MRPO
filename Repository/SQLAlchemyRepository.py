from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .. import DBModel
from PR2.Repository.AbstractRepository import AbstractRepository


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, item):
        self.session.add(item)
        self.session.commit()
        self.session.close()

    def remove(self, item):
        self.session.delete(item)
        self.session.commit()
        self.session.close()

    def get_all(self, model_class):
        items = self.session.query(model_class).all()
        self.session.close()
        return items

    def get_by_id(self, model_class, id):
        item = self.session.query(model_class).filter_by(id=id).first()
        self.session.close()
        return item
