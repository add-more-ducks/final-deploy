from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
#    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable =False)
    email = db.Column(db.String(120), unique=True, nullable =False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    events = db.relationship('Event', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Event(db.Model):
#    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable =False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Event('{self.year}', '{self.headline}')"






"""
    Parts of the Event Class

    month = db.Column(db.Integer, unique=False, nullable =True)
    day = db.Column(db.Integer, unique=False, nullable =True)
    time = db.Column(db.Integer, unique=False, nullable =True)
    endyear = db.Column(db.Integer, unique=False, nullable =True)
    endmonth = db.Column(db.Integer, unique=False, nullable =True)
    endday = db.Column(db.Integer, unique=False, nullable =True)
    endtime = db.Column(db.Integer, unique=False, nullable =True)
    displaydate = db.Column(db.Integer, unique=False, nullable =True)
    userid =  db.Column(db.Integer, unique=False, nullable =True)
"""