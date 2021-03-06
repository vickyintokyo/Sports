"""This landing page of the main app.
From this page all the links will start flowing.

**TODO**
Add an extra view `say_name` that returns your name.
"""
from flask import Flask,request,render_template
import sys
import sqlite3

sys.path.append('../')

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/', methods=['GET', 'POST'])
def lpmain():
    return render_template('index.html')

@app.route('/courts')
def getcourts():
    return 'Welcome to Courts!'

@app.route('/events')
def getevents():
    return 'Welcome to Events!'

@app.route('/signup')
def dosignup():
    return 'Welcome to Signup!'

@app.route('/loginpage')
def loginpage():
    return render_template('signin.html')

@app.route('/signin')
def dosignin():
    from gsignin import index
    return index()

@app.route('/udashboard', methods=['GET', 'POST'])
def getuserdashboard():
    from dboperations import dbcon
    reload(dbcon)
    conn = dbcon.init_db()
    import verifyuid
    uid = request.form['username']
    pwd = request.form['pwd']
    flag = verifyuid.verifypwd(conn,uid,pwd)
    print flag
    if flag:
        return 'Welcome to dashboard!'
    else:
        return 'Error in getting the dashboard'

@app.route('/login')
def glogin():
    from gsignin import login
    return login()

@app.route('/oauth2callback')
def gauthorized():
    from gsignin import authorized
    return authorized()

@app.route('/search', methods=['GET', 'POST'])
def dosearch():
    return 'Welcome to Search!'
