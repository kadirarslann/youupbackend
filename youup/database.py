from datetime import datetime
from youup import db

import uuid

class User(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100),unique=True,nullable=False)
    role = db.Column(db.Integer,nullable=False)
    # def get_id(self):
    #     return (self.username)
    def __repr__(self):
        return f"User('{self.name}', '{self.id}')"

class Reading(db.Model):
    location = db.Column(db.String(150), primary_key=True)
    # def get_id(self):
    #     return (self.username)


class PatientTherapist(db.Model):
    patientid = db.Column(db.String(50), primary_key=True)
    therapistid = db.Column(db.String(50), primary_key=True)
    # def get_id(self):
    #     return (self.username)



class HearthEvent(db.Model):
    id=db.Column(db.String(100), primary_key=True)
    patientid = db.Column(db.String(50),nullable=False)
    value = db.Column(db.Integer,nullable=False)
    date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    # def get_id(self):
    #     return (self.username)



