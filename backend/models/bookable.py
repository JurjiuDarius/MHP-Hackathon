from database import db


class Bookable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    map_id = db.Column(db.Integer, nullable=False, unique=True)
    desk = db.relationship('Desk', backref='bookable', uselist=False, lazy=True)
    room = db.relationship('Room', backref='bookable', uselist=False, lazy=True)
