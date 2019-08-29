#import library
import sqlite3

#open connection to db

connection = sqlite3.connect('library.db')

connection.execute("INSERT INTO Book(ID, Title)" + "values(0, 'example book')")

connection.commit()

#close connection to db
connection.close()