from . import db
from flask_sqlalchemy import SQLAlchemy

class Patients_details (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    sex = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    telephone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    patient_image = db.Column(db.String(250), nullable=True)
    password = db.Column(db.String(50), nullable=False) 
    allergies = db.Column(db.String(50), nullable=True)
    addresses = db.Column(db.String(50), nullable=False)
    medical_details = db.relationship('Medical_details', uselist=False, lazy=True)

class Medical_details(db.Model):
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    person_id = db.ForeignKey('patients_details.id')
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    last_visit = db.Column(db.Date, nullable=True)
    date_created = db.Column(db.Date, nullable=False)
    symptoms = db.Column(db.String(250), nullable=False)
    diagnosis = db.Column(db.String(250), nullable=False)
    med_img = db.Column(db.String(250), nullable=False)