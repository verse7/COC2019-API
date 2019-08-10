import datetime
from . import db
from .User import User

class Event(db.Model):
  __tablename__ = "events"

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(120), nullable=False, unique=True)
  location = db.Column(db.String(255), nullable=False, unique=True)
  manpower_quota = db.Column(db.Integer, nullable=False)
  attendees = db.relationship('User', passive_deletes=True, lazy=True, cascade='all, delete, delete-orphan')
  date_created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

  def __init__(self, title, location, manpower_quota):
    self.title = title
    self.location = location
    self.manpower_quota = manpower_quota