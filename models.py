from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Concert(Base):#Table name (concerts)
  __tablename__= 'concerts'

  #Unique identifier for each concert
  id = Column(Integer,primary_key=True)
  #Foreign key to band
  band_id = Column(Integer,ForeignKey('bands.id'))
  #Foreign key to venue
  venue_id = Column(Integer,ForeignKey('venues.id'))
  #Date for concert
  date = Column(String)

#Relationships to band and venue
  band = relationship("Band",back_populates="concerts")
  venue = relationship("Venue",back_populates="concerts")

  def hometown_show(self):
    #This is to check if concert is in the bands hometown
    return self.venue.city == self.band.hometown
  
  def introduction(self):
    #Creating an introduction message for the concert
    return f"Hello {self.venue.city}!!! We are {self.band.name} and we're from {self.band.hometown}"
  
class Band(Base):
    __tablename__= 'bands'#Table name for bands
    #Unique identifier for band
    id = Column(Integer, primary_key=True)
    #Name of band
    name = Column(String)
    #Hometown of band
    hometown = Column(String)
     #Relationship to concerts
    concerts = relationship("Concert", back_populates='band')

   #This function is to schedule a new concert at a venue on a specified date
    def play_in_venue(self, venue, date):
        new_concert = Concert(band=self, venue=venue, date=date)
        session.add(new_concert)#Adding a new concert
        session.commit()

   #This funtion is for gettin a list of introduction messages for all concerts
    def all_introductions(self):  # Corrected method name
        return [concert.introduction() for concert in self.concerts]
    #This function is for getting a list of venues the band has performed 
    def venues(self):
        return [concert.venue for concert in self.concerts]
    
    @classmethod
    #Tis function returns the band with most perfomances
    def most_performances(cls):
        return max(session.query(cls).all(), key=lambda b: len(b.concerts))

class Venue(Base):
   __tablename__ = 'venues'#Table name for venues

   id = Column(Integer,primary_key=True)#unique identifier for each venue
   #Name of the venue
   name = Column(String)
   #City where the venue will be
   city = Column(String)

   #Relationship to concerts
   concerts = relationship("Concert",back_populates="venue")

   def concert_on(self,date):
      return next((concert for concert in self.concerts if concert.date == date),None)
   
   def most_frequent_band(self):
      band_count={}#Dictionary to count perfomances by band
      for concert in self.concerts:
         #Increment the count for the band
         band_count[concert.band] = band_count.get(concert.band,0) + 1
      return max(band_count,key=band_count.get)