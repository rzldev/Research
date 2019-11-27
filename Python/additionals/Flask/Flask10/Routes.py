from flask import render_template, flash, redirect, url_for, request
from additionals.Flask.Flask10 import app, db, bcrypt, mail
from additionals.Flask.Flask10.forms import RegistrationForm, LoginForm, UpdateForm, PostForm, RequestResetPassword, ResetPassword
from additionals.Flask.Flask10.Models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image
from flask_mail import Message

db.create_all()

@app.route("/")
@app.route("/home")
def home():
    ## Use pagination to sort the post index
    page = request.args.get('page', 1, type=int)
    ## Order post by date_posted
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)

    return render_template('home.html', posts=posts, title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/index")
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts, title='Index')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')

        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('Account created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)

            # Handling for the next page
            next_page = request.args.get('next')

            flash(f'Welcome, {user.username}!', "success")
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Please check email and password!', 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_image(form_picture):
    random_hex = secrets.token_hex(8)
    file_name, file_ext = os.path.splitext(form_picture.filename)
    picture_file_now = random_hex + '.jpg'
    picture_path = os.path.join(
        app.root_path, 'static/image', picture_file_now)
    ouput_size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(ouput_size)
    img.save(picture_path)
    return picture_file_now


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    image_file = url_for('static', filename='image/' +
                         current_user.photo_profile)
    form = UpdateForm()

    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_image(form.picture.data)
            current_user.photo_profile = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account has been updated!', 'success')
        return redirect('account')
    elif request.method == 'get':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('account.html', title='Account', image_file=image_file, form=form)

@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        create_post = Post(title=form.title.data,
                           content=form.content.data, author=current_user)
        db.session.add(create_post)
        db.session.commit()
        flash('Post Created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='Create Post', form=form, legend='Create Post')

@app.route('/post/<int:post_id>')
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', post=post, legend='Update Post', form=form)


@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))

@app.route('/user/<string:username>', methods=['GET', 'POST'])
def user_post(username) :
    user = User.query.filter_by(username=username).first_or_404()
    image_file = url_for('static', filename='image/' + user.photo_profile)
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(per_page=5, page=page)
    return render_template('user_post.html', posts=posts, user=user, image_file=image_file)

## Route for users to reqest token by email
@app.route('/reset-password', methods=['GET', 'POST'])
def request_email() :
    if current_user.is_authenticated :
        return redirect(url_for('home'))

    form = RequestResetPassword()
    if form.validate_on_submit() :
        user = User.query.filter_by(email=form.email.data).first()
        send_token(user)
        flash('An email has been send')
        return redirect('login')
    return render_template('request_reset_password.html', form=form)

## Route for users to reset their password
@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token) :
    if current_user.is_authenticated :
        return redirect('home')

    user = User.verify_reset_token(token)
    if user is None :
        flash('That is an invalid or expired token', 'Warning')
        return redirect('reset_password')

    form = ResetPassword()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash("Your password has been updated!", 'info')
        return redirect(url_for('login'))

    return render_template('reset_password.html', title='Reset Password', form=form)

## Function for send token to user's email
def send_token(user) :
    token = user.get_reset_token()
    message = Message('Password Reset Request', sender='noreply@gmail.com', recipients=[user.email])
    message.body = f"""To reset your password, visit the following link:
    {url_for('reset_password', token=token, _external=True)}
    If you did not make this request then ignore this email"""
    mail.send(message)
