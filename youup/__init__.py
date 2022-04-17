from youup import routes
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

ENV = 'dev'

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/youup'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)
CORS(app)
cors = CORS(app, resource={
    r"/*": {
        "origins": "*"
    }
})
