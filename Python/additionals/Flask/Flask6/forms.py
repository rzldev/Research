from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from additionals.Flask.Flask6.Models import User
## ValidationError Raised when a validator fails to validate its input.

class RegistrationForm(FlaskForm) :
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmation_password = PasswordField('Confirmation Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    ## Create function to check if the user already exist or not
    def validate_username(self, username) :
        user = User.query.filter_by(username=username.data).first()
        if user :
            raise ValidationError('That username is already exist!')

    def validate_email(self, email) :
        user = User.query.filter_by(email=email.data).first()
        if user :
            raise ValidationError('That email is already Exist')

class LoginForm(FlaskForm) :
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
