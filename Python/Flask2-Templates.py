## Import Flask and Template render
from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='additionals/Flask/templates/')

## Create a render template in additionals/html_render_templates
@app.route("/")
def home() :
    return render_template('home.html')

@app.route("/about")
def about () :
    return render_template('about.html')

## Using posts and set title
## See the code in new-home.html and new-about.html
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

@app.route("/new-home")
def new_home() :
    return render_template('new-home.html', posts=posts)

@app.route("/new-about")
def new_about () :
    return render_template('new-about.html', title='New About')

## Using code blocks
## See the code in index1.html and index2.html
@app.route("/index=1")
def index1() :
    return render_template('index1.html', posts=posts, title="Page 1")

@app.route("/index=2")
def index2 () :
    return render_template('index2.html', posts=posts, title='Page 2')

## Using url_for
## url_for in Flask is used for creating a URL to prevent the overhead of
# having to change URLs throughout an application (including in templates)
## See the code in index.html
@app.route("/index")
def index () :
    return render_template('index.html', posts=posts, title='Index')

## Automate debug and run flask
if __name__ == '__main__' :
    app.run(debug=True)
