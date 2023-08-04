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
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all"""
        objects = {}
        if cls:
            for obj in self.__session.query(eval(cls)).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            for clas in models:
                for obj in self.__session.query(eval(clas)).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """comment"""
        self.__session.add(obj)

    def save(self):
        """comment"""
        self.__session.commit()

    def delete(self, obj=None):
        """comment"""
        if obj is None:
            self.__session.delete(obj)

    def reload(self):
        """comment"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
