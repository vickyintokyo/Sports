import sqlite3

def init_db():
    conn = sqlite3.connect('sports.db')
    print "Database created and opened succesfully"
