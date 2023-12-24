#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import Relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = Relationship('Place', backref='user', cascade='all, delete')
    reviews = Relationship('Review', backref='user', cascade='all, delete')
