from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Concert(Base):
  __tablename__= 'concerts'

  id = Column(Integer,primary_key=True)
  band_id = Column(Integer,ForeignKey('bands.id'))
  venue_id = Column(Integer,ForeignKey)('venues.id')
  date = Column(String)

  band = relationship("Band",back_populates="concerts")
  venue = relationship("Venue",back_populates="concerts")

  