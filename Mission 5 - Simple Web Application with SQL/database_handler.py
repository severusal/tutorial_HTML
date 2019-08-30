# database_handler.py

# This file is responsible to:
# - create all tables
# - create connection to database
# - perform CRUD operations

from models import Band, Venue, ConcertBooking, BandBooking


def create_table():
    Band.create_table()

def process_data():
    f = open("raw_data.csv", "r")
    line = f.readline()
    line = f.readline()
    while line:

        row_data = line.split(";")

        venue_name, address, postal, booking_ID, date, band_name, no_of_members, headlining

        b = Band(band_name, no_of_members)
        v = Venue(venue_name, address, postal)
        cb = ConcertBooking(booking_ID, date, venue_name)
        bb = BandBooking(band_name, booking_ID, headlining)

        connection = sqlite3.connection("concert.db")
        connection.execute(b.create_new_record())
        connection.commit()
        connection.close()
        line = f.readline()

    f.close()



process_data()

