#!/usr/bin/python3
"""
This module defines User class to store a user informations

Classes :
    User : inherits from BaseModel
    to store more information related to a user
"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """
    a class to store user informations

    Args:
        first_name (string): the first name of the user
        last_name (string): the last name of the user
        email (string): the email of the user
        password (string): the passowrd of the user
    """

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
