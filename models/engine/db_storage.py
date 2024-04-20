#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
import sqlalchemy
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    """This class manages storage of hbnb models in JSON format"""

    __engine = None
    __session = None
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    def __init__(self):
        db_params = {
            'dialect': 'mysql',
            'driver': 'mysqldb',
            'user': os.environ['HBNB_MYSQL_USER'],
            'password': os.environ['HBNB_MYSQL_PWD'],
            'host': os.environ.get('HBNB_MYSQL_HOST', 'localhost'),
            'database': os.environ['HBNB_MYSQL_DB'],
        }
        url = """mysql+mysqldb://{}:{}@{}/{}""".format(db_params['user'],
                                                       db_params['password'],
                                                       db_params['host'],
                                                       db_params['database']
                                                       )

        self.__engine = create_engine(url, pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        data = {}

        if cls:
            for obj in self.__session.query(cls):
                key = obj.__class__.__name__ + '.' + obj.id
                data[key] = obj
        else:
            for value in DBStorage.classes.values():
                content = self.__session.query(value).all()
                for row in value:
                    key = "{}.{}".format(value.__name__, value.id)
                    objects[key] = value
        return data

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def delete(obj=None):
        "deletes obj if present"
        if obj is None:
            pass
        else:
            self.__session.delete(obj)
        self.save()

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""

        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """ closes the connection to the db instance """
