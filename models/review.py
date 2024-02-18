#!/usr/bin/python3
"""
This module defines Review class to store
a review of a user to a place

Classes :
    Review : inherits from BaseModel
    to store the review of a user to a place
"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Review(BaseModel, Base):
    """
    stores the review of a user to a place

    Args:
        place_id (string): stores Place.id
        user_id (string): stores User_id
        text (string): stores the review
    """

    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    
