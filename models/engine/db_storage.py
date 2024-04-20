#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
import sqlalchemy
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""

    __engine = None
    __session = None

    def __init__(self):
        db_params = {
            'dialect': 'mysql',
            'driver': 'mysqldb',
            'user': os.environ['HBNB_MYSQL_USER'],
            'password': os.environ['HBNB_MYSQL_PWD'],
            'host': os.environ.get('HBNB_MYSQL_HOST', 'localhost'),
            'database': os.environ['HBNB_MYSQL_DB'],
        }
        url = f"""mysql+mysqldb://{db_params['user']}:
{db_params['password']}@{db_params['host']}/
{db_params['database']}"""
        self.__engine = create_engine(url, pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        else:
            Base.metadata.create_all(self.__engine)

        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        obj = {}
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        if cls is None:
            classes = classes
        else:
            classes = classes[cls]
        for cls in classes:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def delete(obj=None):
        "deletes obj if present"
        if obj is None:
            pass
        else:
            self.__session.delete(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        from models.user import User
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
