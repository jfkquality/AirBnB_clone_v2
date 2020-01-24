#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)

        # Use cascade="all, delete" here or on FK constraint in cities??
        # Does it matter where you use single or double quotes?
        # cities = relationship("City", cascade="all, delete", backref="state")
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            """ getter """
            # return self.cities # Old. bad code
            r_v = [];
            objs - models.storage.all();
            for k, v in objs.items():
                if k.split(".")[0] == "City":
                    if self.id == v.state_id:
                        r_v.append(v)
            return(r_v)
