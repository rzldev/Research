## Install Flask-WTF and import it for Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA.
#pip install Flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
## StringField is the base for most of the more complicated fields, and represents an <input type="text">.
## SubmitField represents an <input type="submit">
## BooleanField represents an <input type="checkbox">

## DataRequired will checks the field’s data is ‘truthy’ otherwise stops the validation chain.
## Length will validates the length of a string.
## Email will validates an email address.
## EqualTo will compares the values of two fields

class RegistrationForm(FlaskForm) :
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmation_password = PasswordField('Confirmation Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm) :
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
