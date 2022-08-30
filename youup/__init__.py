


from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
CORS(app)
cors = CORS(app, resource={
    r"/*": {
        "origins": "*"
    }
})
from youup import routes
ENV = 'prod'

app.config['SECRET_KEY'] = ''
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'localpostgreuri'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'remotepostgreuri'
