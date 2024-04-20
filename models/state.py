#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """State class for representing states"""

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          cascade="all, delete-orphan", backref="state")

    @property
    def cities(self):
        """Getter attribute for cities"""
        from models import storage
        cities_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
