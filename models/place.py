#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from os import getenv
from sqlalchemy.orm import relationship

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             nullable=False, primary_key=True),
                      Column("amenity_id", String(60), ForeignKey("amenities.id"),
                             nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            "Review", backref="place", cascade="all, delete, delete-orphan")
        amenities = relationship(
            "Amenity", backref="place_amenity", secondary="place_amenity", viewonly=False)

    else:
        @property
        def reviews(self):
            from models import storage
            from models.review import Review
            reviews = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews

        @property
        def amenities(self):
            from models import storage
            from models.amenity import Amenity
            amenitys = []
            for amen in storage.all(Amenity).values():
                if amen.amenity.id == self.amenity_ids:
                    amenitys.append(amen)
            return amenitys

        @amenities.setter
        def amenities(self, value):
            from models.amenity import Amenity
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
