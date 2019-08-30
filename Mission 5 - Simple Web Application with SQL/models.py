# models.py

# You are to create the following classes in this file
# Band, Venue, ConcertBooking, BandBooking

# Each class should have:
# - necessary attributes
# - static method responsible for table creation
# - methods to generate SQL commands corresponding to insert/update/delete oprations

# You may refer to the below skeleton for the Band class


class Band:
    # init attributes
    def __init__(self, band_name, no_of_members):
        self._band_name = band_name
        self._no_of_members = no_of_members

    # insert necessary getters and setters
    def get_band_name(self):
        return self._band_name

    def get_no_of_members(self):
        return self._no_of_members

    # string output
    def __str__(self):
        result = ""
        result += "Band Name: " + self._band_name
        result += "Number of Members: " + self._no_of_members
        return result

    # SQLite: Create new table
    @staticmethod
    def create_table():
        return """ 
        CREATE TABLE IF NOT EXISTS Band(
            BandName TEXT PRIMARY KEY,
            NoOfMembers INTEGER NOT NULL
        )
        """

    # SQLite: Create new record
    def create_new_record(self):
        return """ 
        INSERT INTO Band
        (BandName, NoOfMembers)
        VALUES
        ('{}',{})
        """.format(self._band_name, self._no_of_members)

    # SQLite: Update record
    def update_record(self):
        return"""
        UPDATE Band SET
        BandName = '{}',NoOfMembers = {}
        WHERE BandName = '{}'
        """.format(self._band_name, self._no_of_members, self._band_name)

    # SQLite: Delete record
    def delete_record(self):
        return"""
        DELETE FROM Band 
        WHERE BandName = '{}'
        """.format(self._band_name)



class Venue:
    def __init__(self, venue_name, address, postal):
        self._venue_name = venue_name
        self._address = address
        self._postal = postal

    def get_vanue_name(self):
        return self._venue_name

    def get_address(self):
        return self._address

    def get_postal(self):
        return self._postal

    # string output
    def __str__(self):
        result = ""
        result += "Venue Name: " + self._venue_name
        result += "Address: " + self._address
        result += "Postal: " + self._postal
        return result

    # SQLite: Create new table
    @staticmethod
    def create_table():
        return """ 
        CREATE TABLE IF NOT EXISTS Venue(
            VenueName TEXT PRIMARY KEY,
            Address TEXT,
            Postal INTEGER NOT NULL
        )
        """

    # SQLite: Create new record
    def create_new_record(self):
        return """ 
        INSERT INTO Venue
        (VenueName, Address, Postal)
        VALUES
        ('{}', '{}', {})
        """.format(self._venue_name, self._address, self._postal)

    # SQLite: Update record
    def update_record(self):
        return"""
        UPDATE Venue SET
        VenueName = '{}', Address = '{}', Postal = {}
        WHERE VenueName = '{}'
        """.format(self._venue_name, self._address, self._postal, self._venue_name)

    # SQLite: Delete record
    def delete_record(self):
        return"""
        DELETE FROM Venue 
        WHERE VenueName = '{}'
        """.format(self._venue_name)




class ConcertBooking:
    def __init__(self, booking_ID, date, venue_name):
        self._booking_ID = booking_ID
        self._date = date
        self._venue_name = venue_name

    def get_booking_ID(self):
        return self._booking_ID

    def get_date(self):
        return self._date

    def get_venue_name(self):
        return self._venue_name

    # string output
    def __str__(self):
        result = ""
        result += "Booking ID: " + self._booking_ID
        result += "Date: " + self._date
        result += "Vanue Name: " + self._venue_name
        return result

    # SQLite: Create new table
    @staticmethod
    def create_table():
        return """ 
        CREATE TABLE IF NOT EXISTS ConcertBooking(
            BookingID TEXT PRIMARY KEY,
            Date TEXT,
            VenueName TEXT,
            FOREIGN KEY (VenueName) REFERENCES Venue(VenueName)
        )
        """

    # SQLite: Create new record
    def create_new_record(self):
        return """ 
        INSERT INTO ConcertBooking
        (BookingID, Date, VenueName)
        VALUES
        ('{}', '{}', '{}')
        """.format(self._booking_ID, self._date, self._venue_name)

    # SQLite: Update record
    def update_record(self):
        return"""
        UPDATE ConcertBooking SET
        BookingID = '{}', Date = '{}', VenueName = '{}'
        WHERE BookingID = '{}'
        """.format(self._booking_ID, self._date, self._venue_name, self._booking_ID)

    # SQLite: Delete record
    def delete_record(self):
        return"""
        DELETE FROM ConcertBooking 
        WHERE BookingID = '{}'
        """.format(self._booking_ID)




class BandBooking:
    def __init__(self, band_name, booking_ID, headlining):
        self._band_name = band_name
        self._booking_ID = booking_ID
        self._headlining = headlining

    def get_band_name(self):
        return self._band_name

    def get_booking_ID(self):
        return self._booking_ID

    def get_headlining(self):
        return self._headlining

    # string output
    def __str__(self):
        result = ""
        result += "Band Name: " + self._band_name
        result += "Booking ID: " + self._booking_ID
        result += "headlining: " + self._headlining
        return result

    # SQLite: Create new table
    @staticmethod
    def create_table():
        return """ 
        CREATE TABLE IF NOT EXISTS BandBooking(
            BandName TEXT,
            BookingID TEXT,
            Headlining INTEGER NOT NULL CHECK (Headlining = 1 OR Headlining = 0),
            PRIMARY KEY (BandName, BookingID),
            FOREIGN KEY (BandName) REFERENCES Band(BandName),
            FOREIGN KEY (BookingID) REFERENCES ConcertBooking(BookingID)

        )
        """

    # SQLite: Create new record
    def create_new_record(self):
        return """ 
        INSERT INTO BandBooking
        (BandName, BookingID, Headlining)
        VALUES
        ('{}', '{}', {})
        """.format(self._band_name, self._booking_ID, self._headlining)

    # SQLite: Update record
    def update_record(self):
        return"""
        UPDATE BandBooking SET
        BandName = '{}', BookingID = '{}', Headlining = {}
        WHERE BandName = '{}'
        """.format(self._band_name, self._booking_ID, self._headlining, self._band_name)

    # SQLite: Delete record
    def delete_record(self):
        return"""
        DELETE FROM BandBooking 
        WHERE BandName = '{}'
        """.format(self._band_name)





# import sqlite3
# connection = sqlite3.connect("concert.db")
# b1 = Band("TheLegend", 2,)
# v1 = Venue("RVHS", "BoonLayAVE", 129959)
# cb1 = ConcertBooking("42931DL", "2019-10-29", "RVHS")
# bb1 = BandBooking("Crazy Elephant", "42932DL", "1")
# connection.execute(cb1.delete_record())
# connection.commit()
# connection.close()