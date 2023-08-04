#!/usr/bin/python3
"""db storage"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from os import getenv

models = [State, City, Amenity, Place, Review, User]


class DBStorage():
    """db storage"""
    __engine = None
    __session = None

    def __init__(self):
        """init class where we create the engine"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_USER")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop(self.__engine)

    def all(self, cls=None):
        """all"""
        objects = {}
        if cls is not None:
            if cls in models:
                _query = self.__session.query(cls).all()
                for obj in _query:
                    key = "{}.{}".format(obj.__name__, obj.id)
                    objects[key] = obj
                return objects
        else:
            for cls in models:
                _query = self.__session.query(cls).all()
                for obj in _query:
                    key = "{}.{}".format(obj.__name__, obj.id)
                    objects[key] = obj

    def new(self, obj):
        """comment"""
        pass

    def save(self):
        """comment"""
        pass

    def delete(self, obj=None):
        """comment"""
        pass

    def reload(self):
        """comment"""
        pass
    # comment cuz i need to push and github didnt save
