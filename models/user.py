#!/usr/bin/python3
"""This is the user class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
"""
Things that might need change:
1. Base inheritance Configuration
do i need to declare base or do
import it from file storage?

fix: in base_model i have to declare base
import base from base_model!
"""


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    # New
    __tablename__ = 'users'

    email = Column(
        String(128),
        nullable=False)
    password = Column(
        String(128),
        nullable=False)
    first_name = Column(
        String(128),
        nullable=True)
    last_name = Column(
        String(128),
        nullable=True)

    places = relationship("Place", backref='user')
    reviews = relationship("Review", backref='user')

    # -------------------------------
    # Old
    # email = ""
    # password = ""
    # first_name = ""
    # last_name = ""
