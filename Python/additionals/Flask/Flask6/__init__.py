from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_bcrypt import Bcrypt

## Flask-Login provides user session management for Flask.
# It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.
## Import Flask-Login
from flask_login import LoginManager

app = Flask(__name__)

secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

db.create_all()

## Create Bcrypt instance
bcrypt = Bcrypt(app)

## Create LoginManager instance
login_manager = LoginManager(app)

## Declare the name of the view to redirect to when the user needs to log in
login_manager.login_view = 'login'

## Set the message for login_view
login_manager.login_message_category = 'info'

from additionals.Flask.Flask6 import Routes
