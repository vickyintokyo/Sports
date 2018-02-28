import sqlite3

def __init__():
    return;

def init_db():
    conn = sqlite3.connect('../../db/sports.db')
    print "Database created and opened succesfully"
    return conn

def main():
    app.run()

if __name__ == '__main__':
   main()
