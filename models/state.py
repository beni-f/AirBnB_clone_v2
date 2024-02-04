#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import Relationship
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    cities = Relationship("City", backref="state", cascade="all, delete")
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Getter method for cities"""
            from models import storage
            from models.city import City
            city_list = []
            all_city = storage.all(City)
            for city in all_city.values():
                city_list.append(city)
            return city_list

