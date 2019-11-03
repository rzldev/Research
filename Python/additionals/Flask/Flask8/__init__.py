from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from additionals.Flask.Flask8 import Routes
