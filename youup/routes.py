
from datetime import datetime
import os
from re import I
import secrets
from urllib import response
import uuid
from flask import render_template, url_for, flash, redirect, request, abort , jsonify , make_response
from youup import app, db
from youup.database import User,HearthEvent,PatientTherapist,Reading


@app.route("/")
@app.route("/home")
def home():
   
    return "donnnududud"

@app.route("/getuser/<int:id>", methods=['GET']) ## ok
def getUser(id):
    user=User.query.filter_by(id=str(id)).first()
    # print(id,"----")
    if(user == None):
        return { 'registered':'false'}
    else:
        response={
            'registered':'true',
            'id':user.id,
            'name':user.name,
            'surname':user.surname,
            'email':user.email,
            'role':user.role
        }
        return  response

@app.route("/createuser", methods=['GET','POST']) ## ok
def createUser():
    data=request.json
    newuser=User(id=data['id'],role=int(data['usertype']),name=data['name'],surname=data['surname'],email=data['email'])
    db.session.add(newuser)
    db.session.commit()
    return {}

@app.route("/assigntherapist", methods=['GET','POST']) ## ok
def assigntherapist():
    data=request.json
    print(data,"----------")
    newduo=PatientTherapist(therapistid=data['therapistid'],patientid=data['patientid'])
    db.session.add(newduo)
    db.session.commit()
    return {}

 
@app.route("/getpatient/<int:therapistid>", methods=['GET']) ## ok
def getPatient(therapistid):
    patients=PatientTherapist.query.filter_by(therapistid=str(therapistid)).all()
    response={}
    for i in range(0,len(patients)):
        user=User.query.filter_by(id=str(patients[i].patientid)).first()
        response[str(i)]={
            'registered':'true',
            'id':user.id,
            'name':user.name,
            'surname':user.surname,
            'email':user.email,
        }
        
    return response

@app.route("/gettherapist/<int:patientid>", methods=['GET']) ## ok
def getTherapist(patientid):
    duo=PatientTherapist.query.filter_by(patientid=str(patientid)).first()
    print(duo)
    if(duo == None):
        return{"registered":'false'}
    else:
        user=User.query.filter_by(id=str(duo.therapistid)).first()
        response={
            'registered':'true',
            'id':user.id,
            'name':user.name,
            'surname':user.surname,
            'email':user.email,
        }
        return response

@app.route("/gettherapists", methods=['GET']) ## ok
def getTherapistAll(): ## ok
    therapists=User.query.filter_by(role=1).all()
    response={}

    response={"0":[None]*len(therapists)}
    for i in range(0,len(therapists)):
        response["0"][i]={
            'id':therapists[i].id,
            'name':therapists[i].name,
            'surname':therapists[i].surname,
            'email':therapists[i].email,
            'role':2,
            
        }
    return response

  
@app.route("/getpatients", methods=['GET']) ## ok
def getPatientsAll():
    patients=User.query.filter_by(role=2).all()
    response={}
    response={"0":[None]*len(patients)}
    for i in range(0,len(patients)):
        response["0"][i]={
            'id':patients[i].id,
            'name':patients[i].name,
            'surname':patients[i].surname,
            'email':patients[i].email,
            'role':2,
        }
 
    return response
      
@app.route("/getpatients/<int:therapistid>", methods=['GET']) ## ok
def getPatientsSpecific(therapistid):
    # patients=User.query.all()
    patients_therapist=PatientTherapist.query.filter_by(therapistid=str(therapistid)).all()
    list=[]
    for i in range(0,len(patients_therapist)):
        list.append(User.query.filter_by(id=str(patients_therapist[i].patientid)).first())
    print(list)
    response={}
    response={"0":[None]*len(list)}
    for i in range(0,len(list)):
        response["0"][i]={
            'id':list[i].id,
            'name':list[i].name,
            'surname':list[i].surname,
            'email':list[i].email,
            'role':2,
        }
    return response

@app.route("/getevents/<int:patientid>", methods=['GET']) ## ok
def getEvents(patientid):
    data=HearthEvent.query.filter_by(patientid=str(patientid)).all()
    response={"0":[None]*len(data)}
    for i in range(0,len(data)):
        response["0"][i]={
            'id':data[i].id,
            'patientid':data[i].patientid,
            'value':data[i].value,
            'date':data[i].date,
        }
    return response

@app.route("/createevent", methods=['GET','POST']) ## ok
def createevent():
    data=request.json
    print(data,"---")
    newevent=HearthEvent(id=uuid.uuid4(),patientid=data['patientid'],value=int(data['value']),date=datetime.now())
    db.session.add(newevent)
    db.session.commit()
    return {}

    
@app.route("/test", methods=['GET','POST'])
def test():
    return {test:'Test'}
