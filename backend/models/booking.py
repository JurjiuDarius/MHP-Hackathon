from database import db
from models.bookable import Bookable


class Booking(db.Model):
    user = db.relationship("User", back_populates="bookings", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    bookable = db.relationship("Bookable", back_populates="bookings", lazy=True)
    bookable_id = db.Column(db.Integer, db.ForeignKey("bookable.id"), primary_key=True)
    date = db.Column(db.Date, nullable=False)
    start = db.Column(db.Time, nullable=False)
    end = db.Column(db.Time, nullable=False)
