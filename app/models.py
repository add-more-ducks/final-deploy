from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

db = SQLAlchemy()

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    userid =  db.Column(db.Integer, unique=False, nullable =True)
    year = db.Column(db.Integer, unique=False, nullable =True)
    month = db.Column(db.Integer, unique=False, nullable =True)
    day = db.Column(db.Integer, unique=False, nullable =True)
    time = db.Column(db.Integer, unique=False, nullable =True)
    endyear = db.Column(db.Integer, unique=False, nullable =True)
    endmonth = db.Column(db.Integer, unique=False, nullable =True)
    endday = db.Column(db.Integer, unique=False, nullable =True)
    endtime = db.Column(db.Integer, unique=False, nullable =True)
    displaydate = db.Column(db.Integer, unique=False, nullable =True)
    text = db.Column(db.String)
    headline = db.Column(db.String)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable =False)
    password = db.Column(db.String(128))
    trust = db.Column(db.Boolean) # Fix this one