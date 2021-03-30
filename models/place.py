#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=True)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") is "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False,)
    else:
        @property
        def reviews(self):
            """ Return list of reviews for FileStorage.
            """
            all_objs = storage.all(Review)
            all_places = []
            for key, value in all_objs.items():
                if value.place_id == self.id:
                    all_places.append(value)
            return all_places

        @property
        def amenities(self):
            """ Return the list of amenities.
            """
            all_objs = storage.all(Amenity)
            all_ams = []
            for key, value in all_objs.items():
                if value.id in self.amenity_ids:
                    all_places.append(value)
            return all_places

        @amenities.setter
        def amenities(self, obj):
            """ Add amenity_id to list.
            """
            if type(obj) == Amenity:
                amenity_ids.append(obj.id)
