import sqlite3

def __init__():
    return;

def init_db1():
    conn = sqlite3.connect('sports.db')
    print "Database created and opened succesfully"
    return conn

def helloworld():
    print "helloworld"

def main():
    app.run()

if __name__ == '__main__':
   main()
