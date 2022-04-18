


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

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/youup'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wargdppuvuwirb:71fc54c56d982f7dc6cf873b278ec3c1f37a51369a77f5078b1be8835fb5a73b@ec2-23-20-224-166.compute-1.amazonaws.com:5432/dk7kk037ggkf6'
