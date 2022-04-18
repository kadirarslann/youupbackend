from youup.database import db
from datetime import datetime
from youup.database import HearthEvent, PatientTherapist, Reading, User
import uuid

db.create_all()
adminemp = User(id="121234221", email="exaasasple0@info.com",
                name="kadir", surname="admin", role=0)  # admin
per1 = User(id="114137001333117408010", email="youupuser1@gmail.com",
            name="user1", surname="user1", role=1)
per2 = User(id="103440533127825966132", email="youupuser2@gmail.com",
            name="user2", surname="user2", role=2)
per3 = User(id="114259231631710528567", email="kadirarslan0000@gmail.com",
            name="kadir", surname="arslan", role=2)
per4 = User(id="113089519994850670119", email="ozguralak8@gmail.com",
            name="ozgur", surname="alak", role=3)


db.session.add_all([adminemp, per1, per2, per3, per4])
db.session.commit()

patient_therapist1 = PatientTherapist(
    patientid="103440533127825966132", therapistid="114137001333117408010")
patient_therapist2 = PatientTherapist(
    patientid="114259231631710528567", therapistid="114137001333117408010")

db.session.add_all([patient_therapist1, patient_therapist2])
db.session.commit()

event1 = HearthEvent(id=uuid.uuid4(), patientid="103440533127825966132",
                     value=121, date=datetime(2020, 11, 3, 1, 10, 0))
event2 = HearthEvent(id=uuid.uuid4(), patientid="103440533127825966132",
                     value=144, date=datetime(2020, 12, 3, 2, 2, 0))
event3 = HearthEvent(id=uuid.uuid4(), patientid="114259231631710528567",
                     value=111, date=datetime(2021, 2, 4, 3, 4, 0))
event4 = HearthEvent(id=uuid.uuid4(), patientid="103440533127825966132",
                     value=163, date=datetime(2021, 3, 5, 4, 14, 0))
event5 = HearthEvent(id=uuid.uuid4(), patientid="114259231631710528567",
                     value=112, date=datetime(2021, 4, 7, 5, 23, 0))
event6 = HearthEvent(id=uuid.uuid4(), patientid="114259231631710528567",
                     value=141, date=datetime(2021, 4, 1, 6, 24, 0))

db.session.add_all([event1, event2, event3, event4, event5, event6])
db.session.commit()
