import sqlite3

def __init__():
    return;

def verifypwd(conn,uid,pwd):
    cursor = conn.cursor();
    print cursor
    obj = cursor.execute("select * from userdata where id="+uid)
    print "came here"
    return true

def main():
    app.run()

if __name__ == '__main__':
   main()
