## Flask is a lightweight WSGI web application framework. 
# It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

## Install Flask
#pip install flask

## Import Flask
from flask import Flask

## Initiate flask into current class
app = Flask(__name__)

## Assigning URL's to functions containing view logic
@app.route("/")
def home() :
    return "Home Page"

## Run Flask manually
# Set Flask environment variable with export
#export FLASK_APP=Flask1-Introduction.py
#flask run

## Giving html structure
@app.route("/about")
def about () :
    return "<h1>About Page</h1>"

## Debug Flask manually
#export FLASK_DEBUG=1
#flask run

## Create a multiple route that handled by the same function
@app.route('/page1')
@app.route('/page2')
def page () :
    return 'Index Page'

## Automate debug and run flask
if __name__ == '__main__' :
    app.run(debug=True)