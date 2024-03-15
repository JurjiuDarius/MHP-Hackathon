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

    def __init__(self, user_id, bookable_id, date, start, end):
        self.user_id = user_id
        self.bookable_id = bookable_id
        self.date = date
        self.start = start
        self.end = end

    def serialize(self):
        return {
            "user_id": self.user_id,
            "bookable_id": self.bookable_id,
            "date": self.date,
            "start": self.start,
            "end": self.end,
        }
