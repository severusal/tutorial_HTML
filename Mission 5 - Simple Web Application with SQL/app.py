# app.py

# This file is responsible to handle flask operations
from flask import Flask, render_template, url_for, redirect, request
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

@app.route("/edit_concert_booking/<int:booking_id>", methods=["GET", "POST"])
def edit_concert_booking(booking_id):
    if request.method =="GET":
    #read daat from database
        connection = sqlite3.connect("concert.db")
        cursor = connection.execute("SELECT * FROM ConcertBooking WHERE BookingID={}".format(booking_id))
        data = cursor.fetchone()
        cursor.close()
        connection.close()

        print(data)
        if data is None:
            return "enter a valid booking ID!"
            
        else:
            c = ConcertBooking(data[0], data[1], data[2])

        return render_template("edit_booking.html", c=c)
    else:
        new_date = request.form["date"]
        new_venue_name = request.form["venue_name"]
        c = ConcertBooking(booking_id, new_date, new_venue_name)

        connection = sqlite3.connect("concert.db")
        connection.execute(c.update_record())
        connection.commit()
        connection.close()
        return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True)