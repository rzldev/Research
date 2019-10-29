from flask import render_template, flash, redirect, url_for, request
from additionals.Flask.Flask7 import app, db, bcrypt
from additionals.Flask.Flask7.forms import RegistrationForm, LoginForm, UpdateForm
from additionals.Flask.Flask7.Models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os

## To resize the image using pillow
from PIL import Image

# db.create_all()

posts = [
    {
        'author' : 'Bruce Wayne',
        'title' : 'Rise Of The Batman',
        'content' : 'First Post Content',
        'date_posted' : 'Oct 20, 2020'
    },
    {
        'author' : 'Barry Allen',
        'title' : 'The Flash Flashpoint Paradox',
        'content' : 'Second Post Content',
        'date_posted' : 'Oct 25, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home() :
    return render_template('home.html', posts=posts, title='Home')

@app.route("/about")
def about () :
    return render_template('about.html', title='About')

@app.route("/index")
def index () :
    return render_template('index.html', posts=posts, title='Index')

@app.route("/index=1")
def index1() :
    return render_template('index1.html', posts=posts, title="Page 1")

@app.route("/index=2")
def index2 () :
    return render_template('index2.html', posts=posts, title='Page 2')

@app.route("/register", methods=['GET', 'POST'])
def register () :
    form = RegistrationForm()

    ## Checking if the user is already login or not
    if current_user.is_authenticated :
        return redirect(url_for('home'))

    if form.validate_on_submit() :

        ## Hashing password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        ## Insert user into database
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash(f'Account created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login () :
    form = LoginForm()

    ## Checking if the user is already login or not
    if current_user.is_authenticated :
        return redirect(url_for('home'))

    if form.validate_on_submit() :
        user = User.query.filter_by(email=form.email.data).first()

        ## Create a login session for user(Check if the email and password are correct)
        if user and bcrypt.check_password_hash(user.password, form.password.data) :
            login_user(user, remember=form.remember.data)

            ## Handling for the next page
            next_page = request.args.get('next')

            flash(f'Welcome, {user.username}!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else :
            flash(f'Login unsuccessful. Please check email and password!', 'danger')

    return render_template('login.html', title='Login', form = form)

## For admin to check user list
@app.route("/user-list")
def user_list() :
    return render_template('user_list.html', posts=User.query.all(), title='Restricted')

@app.route('/logout')
def logout() :
    logout_user()
    return redirect(url_for('home'))

## Create function to save the image_file
def save_image(form_picture) :
    random_hex = secrets.token_hex(8)
    file_name, file_ext = os.path.splitext(form_picture.filename)
    picture_file_now = random_hex + '.jpg'
    picture_path = os.path.join(app.root_path, 'static/image', picture_file_now)

    ## Set the size of the Image
    ouput_size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(ouput_size)

    img.save(picture_path)
    return picture_file_now

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account() :

    ## Set image for photo profile
    image_file = url_for('static', filename='image/' + current_user.photo_profile)

    ## Set update form
    form = UpdateForm()

    ## Update the user data
    if form.validate_on_submit() :
        ## Save image_file
        if form.picture.data :
            picture_file = save_image(form.picture.data)
            current_user.photo_profile = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account has been updated!', 'success')
        return redirect('account')
    elif request.method == 'get' :
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('account.html', title='Account', image_file=image_file, form=form)
