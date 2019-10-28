from flask_sqlalchemy import SQLAlchemy
from additionals.Flask.Flask6 import app

## Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for your application.
## Install Flask-bcrypt
#pip install flask-bcrypt

## Import Flask-Bcrypt
from flask_bcrypt import Bcrypt

## Create Bcrypt instance
bcrypt = Bcrypt()

## Using hash on password
password = 'Password'
print(password + ' = ' + str(bcrypt.generate_password_hash(password)))
print(password + ' = ' + str(bcrypt.generate_password_hash(password).decode('utf-8')))
print()

## Checking
hashed_pass = bcrypt.generate_password_hash(password).decode('utf-8')
print(bcrypt.check_password_hash(hashed_pass, 'password'))
print(bcrypt.check_password_hash(hashed_pass, 'Password'))
print()

## Automate debug and run flask
if __name__ == '__main__' :
    app.run(debug=True)
