# app.py

# This file is responsible to handle flask operations
from flask import Flask, render_template, url_for
import sqlite3
from database_handler import execute_sql
from models import Band, BandBooking, ConcertBooking, Venue
app = Flask(__name__)


@app.route("/")
def index():
    connection = sqlite3.connect("concert.db")
    cursor = connection.execute("SELECT * FROM ConcertBooking")
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    print(data)
    #process the data
    all_bookings = []
    for record in data:
        c = ConcertBooking(record[0], record[1], record[2])
        all_bookings.append(c)


    return render_template("index.html", all_bookings=all_bookings)

@app.route("/edit_concert_booking/<int:booking_id>")
def edit_concert_booking(booking_id):
    return str(booking_id)

if __name__ == "__main__":
    app.run(debug=True)