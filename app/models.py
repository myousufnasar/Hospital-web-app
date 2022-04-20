from . import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import datetime
from flask_login import UserMixin


class Users (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=True)
    lastname = db.Column(db.String(50), nullable=True)
    sex = db.Column(db.String(50), nullable=True)
    address = db.Column(db.String(50), nullable=True)
    dob = db.Column(db.String(50), nullable=True)
    telephone = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    patient_image = db.Column(db.String(250), nullable=True)
    password = db.Column(db.String(50), nullable=True) 
    allergies = db.Column(db.String(500), nullable=True)
    # change staff to patient later this is for testing purpose only
    role = db.Column(db.String(), default='Staff')
    medical_details = db.relationship('Medical_details', backref='users', uselist=False, lazy=True)
    time = db.Column(db.DateTime(timezone=True), default=func.now())



class Medical_details(db.Model):
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    height = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    last_visit = db.Column(db.Date, nullable=True)
    date_created = db.Column(db.Date, nullable=True)
    symptoms = db.Column(db.String(250), nullable=True)
    diagnosis = db.Column(db.String(250), nullable=True)
    med_img = db.Column(db.String(250), nullable=True)


class Diagnosed_history(db.Model):
    id = db.Column(db.Integer,primary_key=True, nullable=True)
    firstname = db.Column(db.String(250), nullable=True)
    lastname = db.Column(db.String(250), nullable=True)
    date = db.Column(db.String(250), nullable=True)
    diagnosed = db.Column(db.String(), nullable=True)
    symptoms = db.Column(db.String(), nullable=True)   


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
