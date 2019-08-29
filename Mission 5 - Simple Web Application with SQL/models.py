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


import sqlite3
connection = sqlite3.connect("concert.db")
b1 = Band("TheLegend", 3)
connection.execute(b1.create_table())
connection.commit()
connection.close()