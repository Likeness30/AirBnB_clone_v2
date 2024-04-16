#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = ""
