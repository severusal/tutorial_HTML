# database_handler.py

# This file is responsible to:
# - create all tables
# - create connection to database
# - perform CRUD operations

from models import Band, Venue, ConcertBooking, BandBooking
import sqlite3

def execute_sql(sql_command):
    connection = sqlite3.connect("concert.db")
    try:
        connection.execute(sql_command)
        connection.commit()
    except sqlite3.IntegrityError:  # sqlite duplicate entry error
        print("Duplicate data found, no additional entry recorded.")
    connection.close()


def create_tables():
    # method 1
    execute_sql(Band.create_table())
    execute_sql(Venue.create_table())
    execute_sql(ConcertBooking.create_table())
    execute_sql(BandBooking.create_table())

    # method 2
    create_table_sql = [
        Band.create_table(),
        Venue.create_table(),
        ConcertBooking.create_table(),
        BandBooking.create_table()
    ]

    for sql in create_table_sql:
        execute_sql(sql)


# create_tables()


def process_data():
    f = open("raw_data.csv", "r")
    line = f.readline()  # header line, which contain no meaningful data
    line = f.readline()[:-1]  # read from 2nd line onwards, real data
    while line:
        row_data = line.split(";")

        venue_name, addr, postal, booking_id, date, band_name, no_of_members, headlining = row_data
        print(headlining)
        if headlining == "Y":
            headlining = 1
        else:
            headlining = 0
        print(headlining)


        b = Band(band_name, no_of_members)
        v = Venue(venue_name, addr, postal)
        c = ConcertBooking(booking_id, date, venue_name)
        bb = BandBooking(booking_id, band_name, headlining)

        list_of_objs = [b, v, c, bb]

        for ob in list_of_objs:
            execute_sql(ob.create_new_record())

        line = f.readline()[:-1]

    f.close()


# process_data()
