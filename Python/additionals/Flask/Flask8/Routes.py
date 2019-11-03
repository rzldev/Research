from flask import render_template, flash, redirect, url_for, request
from additionals.Flask.Flask8 import app, db, bcrypt
from additionals.Flask.Flask8.forms import RegistrationForm, LoginForm, UpdateForm, PostForm
from additionals.Flask.Flask8.Models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image

db.create_all()


@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
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

            flash(f'Welcome, {user.username}!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Please check email and password!', 'danger')

    return render_template('login.html', title='Login', form=form)

# For admin to check user list
@app.route("/user-list")
def user_list():
    return render_template('user_list.html', posts=User.query.all(), title='Restricted')


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

# Route for create a new post
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

# Route for a single post
@app.route('/post/<int:post_id>')
@login_required
def post(post_id):
    # Use a not found statement
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


# Route for a single post
@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    # Use a forbidden statement
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
    # Use a forbidden statement
    if post.author != current_user:
        abort(403)
    form = PostForm()
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))
