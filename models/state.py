#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # Use cascade="all, delete" here or on FK constraint in cities??
    # Does it matter where you use single or double quotes?
    # cities = relationship("City", cascade="all, delete", backref="state")
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """ getter """
        return self.cities
