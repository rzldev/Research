from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

## Install Flask_mail
#pip install Flask-Mail

## Flask-Mail extension provides a simple interface to set up SMTP with your Flask application
# and to send messages from your views and scripts.
from flask_mail import Mail
import os

app = Flask(__name__)

secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

## Config for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('Email')
app.config['MAIL_PASSWORD'] = os.environ.get('Password')
mail = Mail(app)

from additionals.Flask.Flask10 import Routes
