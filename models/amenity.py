#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy import ForeignKey, MetaData, Table
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenity = Table('place_amenity', metadata=Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'), nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'), nullable=False)
                          )
    place_amenities = relationship('Place', secondary=place_amenity)
