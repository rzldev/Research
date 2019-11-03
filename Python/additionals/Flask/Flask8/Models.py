from additionals.Flask.Flask8 import db
from datetime import datetime
from additionals.Flask.Flask8 import login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin) :
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

@login_manager.user_loader
def load_user(user_id) :
    return User.query.get(int(user_id))
