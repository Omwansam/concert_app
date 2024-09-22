from database import session
from models import Band, Venue, Concert

# Input your examples
'''band_name = 'The Beatles'
hometown = 'England'
venue_name = 'Manchester stadium'
city = 'Manchester'
concert_date = '2024-09-21'''

def add_concert(band_name, hometown, venue_name, city, concert_date):
    # Check if the band already exists
    band = session.query(Band).filter_by(name=band_name, hometown=hometown).first()
    if not band:
        band = Band(name=band_name, hometown=hometown)
        session.add(band)

    # Check if the venue already exists
    venue = session.query(Venue).filter_by(name=venue_name, city=city).first()
    if not venue:
        venue = Venue(name=venue_name, city=city)
        session.add(venue)

    # Check if the concert already exists
    concert = session.query(Concert).filter_by(band=band, venue=venue, date=concert_date).first()
    if not concert:
        concert = Concert(band=band, venue=venue, date=concert_date)
        session.add(concert)

add_concert('The Beatles','England','Manchester Stadium','Manchester','2024-09-21')
add_concert('Queen','England','Bedford Stadium','Bedford','2024-10-16')
session.commit()

# Testing
first_band = session.query(Band).first()
if first_band:
    print(first_band.venues())
    print(first_band.all_introductions())
    
    if first_band.concerts:
        print(first_band.concerts[0].introduction())
    else:
        print("No concerts found for this band.")
else:
    print("No bands found in the database.")
