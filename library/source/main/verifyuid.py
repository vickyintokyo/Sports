import sqlite3

def __init__():
    return;

def verifypwd(conn,uid,pwd):
    c = conn.cursor();
    c.execute("select pwd from userdata where name='"+uid+"'")
    rs = c.fetchone()
    if rs == None:
        return False;
    else:
        if pwd == rs[0]:
            return True
        else:
            return False

def main():
    app.run()

if __name__ == '__main__':
   main()
