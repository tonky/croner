"""Person model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from croner.model.meta import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    login = Column(String(100))
    passwd = Column(String(100))
    email = Column(String(100))

    def __init__(self, name='', email='', login=''):
        self.name = name
        self.email = email
        self.login = login

    def password(self, pw):
        self.passwd = pw

    def __repr__(self):
        return "<User('%s')" % self.login
