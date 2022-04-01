from . import db
from flask_sqlalchemy import SQLAlchemy
import datetime



class Users (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50), nullable=True)
    LastName = db.Column(db.String(50), nullable=True)
    sex = db.Column(db.String(50), nullable=True)
    address = db.Column(db.String(50), nullable=True)
    dob = db.Column(db.String(50), nullable=True)
    telephone = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    patient_image = db.Column(db.String(250), nullable=True)
    password = db.Column(db.String(50), nullable=True) 
    allergies = db.Column(db.String(500), nullable=True)
    medical_details = db.relationship('Medical_details', backref='person', uselist=False, lazy=True)
    time = db.Column(db.DateTime(timezone=True), default=func.now())



class Medical_details(db.Model):
    id = db.Column(db.Integer,primary_key=True, nullable=True)
    person_id = db.ForeignKey(db.Integer, 'users.id')
    height = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    last_visit = db.Column(db.Date, nullable=True)
    date_created = db.Column(db.Date, nullable=True)
    symptoms = db.Column(db.String(250), nullable=True)
    diagnosis = db.Column(db.String(250), nullable=True)
    med_img = db.Column(db.String(250), nullable=True)


# class Appointments(db.Model):
#     id = db.Column(db.Integer,primary_key=True, nullable=True)
#     person_id = db.ForeignKey('patients_details.id')
#     height = db.Column(db.Integer, nullable=True)
#     weight = db.Column(db.Integer, nullable=True)
#     last_visit = db.Column(db.Date, nullable=True)
#     date_created = db.Column(db.Date, nullable=True)
#     symptoms = db.Column(db.String(250), nullable=True)
#     diagnosis = db.Column(db.String(250), nullable=True)
#     med_img = db.Column(db.String(250), nullable=True)
