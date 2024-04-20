#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Integer, Column, DateTime, ForeignKey
from datetime import datetime


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'Cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(128), nullable=False)
    state_id.constraint = ForeignKey('states.id')
    created_at = Column(DateTime, nullable=False,
                        primary_key=True, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False,
                        primary_key=True, default=datetime.utcnow())
