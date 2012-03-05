"""SQLAlchemy Metadata and Session object"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

__all__ = ['Base', 'Session']

# SQLAlchemy session manager. Updated by model.init_model()
Session = scoped_session(sessionmaker())

# The declarative Base
Base = declarative_base()

def fixture(ss):
    from croner.model import User
    u = User(name="Joe", login="joe", email="joe@doe.com")
    u.password('1')
    ss.add(u)

    u2 = User(name="Alicia", login="alicia", email="alicia@doe.com")
    u2.password('2')
    ss.add(u2)
