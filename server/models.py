from sqlalchemy import Column, Integer, Float, String
from sqlalchemy_serializer import SerializerMixin
from app import db

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'

    id = Column(Integer, primary_key=True)
    magnitude = Column(Float)
    location = Column(String)
    year = Column(Integer)

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
