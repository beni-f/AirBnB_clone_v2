#!/usr/bin/python3
"""
    An engine to store data in form of database
"""
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    __engine = None
    __session = None
    def __init__(self):
        """Initialization"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER,               HBNB_MYSQL_PWD,                     HBNB_MYSQL_HOST,                       HBNB_MYSQL_DB),              pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)
    def all(self, cls=None):
        """ query and return all """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session__.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            obj_lists = [State, City, User, Place, Review, Amenity]
            for clase in obj_lists:
                query = self.__session__.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)
        
    def new(self, obj):
        """Add the object to the current database session"""
        self.__session__.add(obj)
    def save(self):
        """commit all changes of the current database session"""
        self.__session__.commit()
    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session__.delete()
    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session__ = Session()
    def close(self):
        """Close session"""
        self.__session.close()