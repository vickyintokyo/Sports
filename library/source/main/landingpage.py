"""This is the most basic example of a Flask application.

As you can see we need just three things:
 * Create an app object from the Flask class.
 * Define a route to match (in this case the root '/' path)
 * Link it to a specific "view".

A View is a simple Python function that will take care of the work to be
done for a specified path. The function should return a String that will
be returned back to the client in form of HTML.

In this case the function `hello_world` is the view in charge of processing
requests to '/' (_example.com/_).

**TODO**
Add an extra view `say_name` that returns your name.
"""
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def lpmain():
    #return 'Welcome to Vikram world!'
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

@app.route('/signin')
def dosignin():
    return 'Welcome to SignIn!'

@app.route('/search', methods=['GET', 'POST'])
def dosearch():
    return 'Welcome to Search!'
