from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from additionals.Flask.Flask9.Models import User

class RegistrationForm(FlaskForm) :
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmation_password = PasswordField('Confirmation Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

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


class UpdateForm(FlaskForm) :
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Photo', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Update')

    ## Create function to check if the user already exist or not
    def validate_username(self, username) :
        if username.data is current_user.username :
            user = User.query.filter_by(username=username.data).first()
            if user :
                raise ValidationError('That username is already exist1!')
        elif username.data is current_user.username and username.data is not User.username :
            user = User.query.filter_by(username=username.data).first()
            if user :
                raise ValidationError('That username is already exist!')

    def validate_email(self, email) :
        if email.data is current_user.email :
            user = User.query.filter_by(email=email.data).first()
            if user :
                raise ValidationError('That email is already exist1!')
        elif email.data is current_user.email and email.data is not User.email:
            user = User.query.filter_by(email=email.data).first()
            if user :
                raise ValidationError('That email is already exist!')


class PostForm(FlaskForm) :
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
