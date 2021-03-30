#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete")

    @property
    def cities(self):
        """ Get the list of City instances in the calling state.
        """
        all_objs = storage.all(City)
        all_cities = []
        for key, value in all_objs.items():
            if value.state_id == self.id:
                all_cities.append(value)
        return all_cities