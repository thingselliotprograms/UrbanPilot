from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import *
from app import db



#db = SQLAlchemy()

#Base = declarative_base()

#engine = create_engine("postgresql://postgres:database@localhost/urban_pilot")

class InfoSubmission(db.Model):
    __tablename__ = 'info_submissions'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String())
    mname = db.Column(db.String())
    lname = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    zip = db.Column(db.Integer)
    city = db.Column(db.String())
    county = db.Column(db.String())
    state = db.Column(db.String())

    def __init__(self, email, zip, fname, mname, lname, city, county, state):
        self.email = email
        self.zip = zip
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.city = city
        self.county = county
        self.state = state

        pass

    @property
    def toJSON(self):
        return {
            'id': self.id,
            'fname': self.fname,
            'mname': self.mname,
            'lname': self.lname,
            'zip': self.zip,
            'email':self.email
            }

class LocationRanks(db.Model):
    __tablename__ = "location_ranks"

    id = db.Column(db.Integer, primary_key=True)
    zip = db.Column(db.Integer, unique=True)
    total = db.Column(db.Integer)
    portion = db.Column(db.Numeric)

    def __init__(self, zip, total, portion):
        self.zip = zip
        self.total = total
        self. portion = portion
