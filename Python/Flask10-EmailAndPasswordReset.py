from flask_sqlalchemy import SQLAlchemy
from additionals.Flask.Flask10 import app

## Automate debug and run flask
if __name__ == '__main__' :
    app.run(debug=True)
