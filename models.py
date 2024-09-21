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

  def hometown_show(self):
    return self.venue.city == self.band.hometown
  
  def introduction(self):
    return f"Hello {self.venue.city}!!! We are {self.band.name} and we're from {self.band.hometown}"
  
  class Band(Base):
    __tablename__= 'bands'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    hometown = Column(String)

    concerts = relationship("Concert",back_populates='band')

    def play_in_venue(self,venue,date):
      new_concert = Concert(band=self,venue=venue,date=date)
      session.add(new_concert)
      session.commit()

    def all_instructions(self):
        return [concert.introduction() for concert in self.concerts]
    
    def venues(self):
        return [concert.venue for concert in self.concerts]
    
    @classmethod
    def most_perfomances(cls):
       return max(session.query(cls).all(),key=lambda b: len(b.concerts))