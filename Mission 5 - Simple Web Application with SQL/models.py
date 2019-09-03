# models.py

# You are to create the following classes in this file
# Band, Venue, ConcertBooking, BandBooking

# Each class should have:
# - necessary attributes
# - static method responsible for table creation
# - methods to generate SQL commands corresponding to insert/update/delete operations

# You may refer to the below skeleton for the Band class


import sqlite3


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
        result += "No of Members: " + self._no_of_members
        return result

    # SQLite: Create new table
    @staticmethod
    def create_table():
        return """
        CREATE TABLE IF NOT EXISTS Band (
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
        ('{}', {})
        """.format(self._band_name, self._no_of_members)

    # SQLite: Update record
    def update_record(self):
        return """
        UPDATE Band SET
        BandName = '{}', NoOfMembers = {}
        WHERE BandName = '{}'
        """.format(self._band_name,
                   self._no_of_members,
                   self._band_name)

    # SQLite: Delete record
    def delete_record(self):
        return """
        DELETE FROM Band
        WHERE BandName = '{}'
        """.format(self._band_name)


class Venue:
    # init attributes
    def __init__(self, venue_name, addr, postal):
        self._venue_name = venue_name
        self._addr = addr
        self._postal = postal

    # insert necessary getters and setters
    def get_venue_name(self):
        return self._venue_name

    def get_addr(self):
        return self._addr

    def get_postal(self):
        return self._postal

    # string output
    def __str__(self):
        result = ""
        result += "Venue Name: " + self._venue_name
        result += "Address: " + self._addr
        result += "Postal: " + self._postal
        return result

    # SQLite: Create new table
    @staticmethod
    def create_table():
        return """
        CREATE TABLE IF NOT EXISTS Venue (
            VenueName TEXT PRIMARY KEY,
            Addr TEXT NOT NULL,
            Postal INTEGER NOT NULL CHECK (Postal <= 999999)
        )
        """

    # SQLite: Create new record
    def create_new_record(self):
        return """
        INSERT INTO Venue
        (VenueName, Addr, Postal)
        VALUES
        ('{}', '{}', {})
        """.format(self._venue_name, self._addr, self._postal)

    # SQLite: Update record
    def update_record(self):
        return """
        UPDATE Venue SET
        VenueName = '{}', Addr = '{}', Postal = {}
        WHERE VenueName = '{}'
        """.format(self._venue_name,
                   self._addr,
                   self._postal,
                   self._venue_name)

    # SQLite: Delete record
    def delete_record(self):
        return """
        DELETE FROM Venue
        WHERE VenueName = '{}'
        """.format(self._venue_name)


class ConcertBooking:
    # init attributes
    def __init__(self, booking_id, date, venue_name):
        self._booking_id = booking_id
        self._date = date
        self._venue_name = venue_name

    # insert necessary getters and setters
    def get_booking_id(self):
        return self._booking_id

    def get_date(self):
        return self._date

    def get_venue_name(self):
        return self._venue_name

    # string output
    def __str__(self):
        result = ""
        result += "Booking ID: " + self._booking_id
        result += "Date: " + self._date
        result += "Venue Name: " + self._venue_name
        return result

    # SQLite: Create new table
    @staticmethod
    def create_table():
        return """
        CREATE TABLE IF NOT EXISTS ConcertBooking (
            BookingID INTEGER PRIMARY KEY AUTOINCREMENT,
            Date TEXT NOT NULL,
            VenueName TEXT NOT NULL,
            FOREIGN KEY (VenueName) REFERENCES Venue(VenueName)
        )
        """

    # SQLite: Create new record
    def create_new_record(self):
        return """
        INSERT INTO ConcertBooking
        (BookingID, Date, VenueName)
        VALUES
        ({}, '{}', '{}')
        """.format(self._booking_id, self._date, self._venue_name)

    # SQLite: Update record
    def update_record(self):
        return """
        UPDATE ConcertBooking SET
        BookingID = {}, Date = '{}', VenueName = '{}'
        WHERE BookingID = {}
        """.format(self._booking_id,
                   self._date,
                   self._venue_name,
                   self._booking_id)

    # SQLite: Delete record
    def delete_record(self):
        return """
        DELETE FROM ConcertBooking
        WHERE BookingID = {}
        """.format(self._booking_id)


class BandBooking:
    # init attributes
    def __init__(self, booking_id, band_name, headlining):
        self._booking_id = booking_id
        self._band_name = band_name
        self._headlining = headlining

    # insert necessary getters and setters
    def get_booking_id(self):
        return self._booking_id

    def get_band_name(self):
        return self._band_name

    def get_headlining(self):
        return self._headlining

    # string output
    def __str__(self):
        result = ""
        result += "Booking ID: " + self._booking_id
        result += "Band Name: " + self._band_name
        result += "Headlining: " + self._headlining
        return result

    # SQLite: Create new table
    @staticmethod
    def create_table():
        return """
        CREATE TABLE IF NOT EXISTS BandBooking (
            BookingID INTEGER,
            BandName TEXT,
            Headlining INTEGER NOT NULL CHECK (Headlining = 1 OR Headlining = 0),
            PRIMARY KEY (BookingID, BandName),
            FOREIGN KEY (BookingID) REFERENCES ConcertBooking(BookingID),
            FOREIGN KEY (BandName) REFERENCES Band(BandName)
        )
        """

    # SQLite: Create new record
    def create_new_record(self):
        return """
        INSERT INTO BandBooking
        (BookingID, BandName, Headlining)
        VALUES
        ({}, '{}', {})
        """.format(self._booking_id, self._band_name, self._headlining)

    # SQLite: Update record
    def update_record(self):
        return """
        UPDATE BandBooking SET
        BookingID = {}, BandName = '{}', Headlining = {}
        WHERE BookingID = {} AND BandName = '{}'
        """.format(self._booking_id,
                   self._band_name,
                   self._headlining,
                   self._booking_id,
                   self._band_name)

    # SQLite: Delete record
    def delete_record(self):
        return """
        DELETE FROM BandBooking
        WHERE BookingID = {} AND BandName = '{}'
        """.format(self._booking_id, self._band_name)


# testing while we code
# connection = sqlite3.connect("concert.db")
# bb1 = BandBooking(1, "BName", 0)
# connection.execute(bb1.delete_record())
# connection.commit()
# connection.close()
