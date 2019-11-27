from additionals.Flask.Flask10 import db, app
from datetime import datetime
from additionals.Flask.Flask10 import login_manager
from flask_login import UserMixin

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
## TimedJSONWebSignatureSerializer works like the regular JSONWebSignatureSerializer
# but also records the time of the signing and can be used to expire signatures

class User(db.Model, UserMixin) :
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    photo_profile = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(20), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    ## Function to get token for reset password
    def get_reset_token(self, expires_esc=1800) :
        s = Serializer(app.config['SECRET_KEY'], expires_esc)

        ## Serializer.dumps returns a signed string serialized with the internal serializer
        return s.dumps({'user_id' : self.id}).decode('utf-8')

    ## staticmethod() is considered un-Pythonic way of creating a static function.
    ## Function to verify token for reset password
    @staticmethod
    def verify_reset_token(token) :
        s = Serializer(app.config['SECRET_KEY'])
        try :
            user_id = s.loads(token)['user_id']
        except :
            return None
        return User.query.get(user_id)


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
