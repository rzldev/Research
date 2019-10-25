from flask import Flask, render_template
import secrets
## The secrets module is used for generating cryptographically strong random numbers
# suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

## Import forms.py
from additionals.Flask.forms import RegistrationForm, LoginForm

from flask import flash, redirect, url_for
## Flash can be used to give feedback to a user(succes or not)

app = Flask(__name__, template_folder='additionals/Flask/templates/')

secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key
## SECERT_KEY >> A secret key that will be used for securely signing the session cookie
# and can be used for any other security related needs by extensions or your application.

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

## methods >> to accepted HTTP Methods
## validate_on_submit >> will check if it is a POST request and if it is valid

## Automate debug and run flask
if __name__ == '__main__' :
    app.run(debug=True)
