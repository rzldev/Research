## Install Flask-SQLAlchemy
#pip install flask-sqlalchemy
## Import Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, flash, redirect, url_for
import secrets
from additionals.Flask.forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__, template_folder='additionals/Flask/templates/')

secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key
## Config SQL database path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
## Create database instance
db = SQLAlchemy(app)

## Create class User and Post for databse structure
class User(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    photo_profile = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(20), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__ (self) :
        return f"User('{self.username}', '{self.email}', '{self.photo_profile}')"

class Post(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) :
        return f"Post('{self.title}', '{self.date_posted}', '{self.content}')"


## db.Model is the baseclass for all your models
## db.Column is to define a your column.
## db.relationship to expressed the realtionship between function
## backref is a simple way to also declare a new property on the Address class.
## lazy defines when SQLAlchemy will load the data from the database

db.drop_all()

## Insert Users
db.create_all()
bruce = User(username='Bruce Wayne', email='Bruce@Richman.com', password='Batman')
db.session.add(bruce)
clark = User(username='Clark Kent', email='Kent@Superman.com', password='Superman')
db.session.add(clark)
db.session.commit()

## Print the table
print(User.query.all())

print()

## Print some specific items
print(User.query.first())
print(User.query.filter_by(username='Bruce Wayne').all())
print(User.query.filter_by(username='Bruce Wayne').first())

print()

## Set user
user = User.query.filter_by(username='Bruce Wayne').first()
print(str(user.id))

print()

## Insert Posts
post1 = Post(title='The Arkham Knight', content='Arkham\'s Content', user_id=user.id)
db.session.add(post1)
post2 = Post(title='The Arham Asylum', content='Asylum\'s Content', user_id=user.id)
db.session.add(post2)
db.session.commit()

## Print posts
print(user.posts)

print()

## Print post's title
for post in user.posts :
    print(post.title)

print()

## Set post
post = Post.query.first()
print(post)
print(post.id)

print()

## Print post's author
print(post.author)
print()

## To delete all table
db.drop_all()

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
    return render_template('my-home.html', posts=posts, title='Home')

@app.route("/about")
def about () :
    return render_template('my-about.html', title='About')

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
    if form.validate_on_submit() :
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login () :
    form = LoginForm()
    if form.validate_on_submit() :
        if form.email.data == 'user@gmail.com' and form.password.data == 'password' :
            flash(f'Welcome, {form.email.data}!', 'success')
            return redirect(url_for('home'))
        else :
            flash(f'Login unsuccessful. Please check email and password!', 'danger')
    return render_template('login.html', title='Login', form = form)

## Automate debug and run flask
if __name__ == '__main__' :
    app.run(debug=True)
