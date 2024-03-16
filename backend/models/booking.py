from database import db
from utils.json import json_serial_date


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship("User", back_populates="bookings", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    bookable = db.relationship("Bookable", back_populates="bookings", lazy=True)
    bookable_id = db.Column(db.String, db.ForeignKey("bookable.id"))
    date = db.Column(db.Date, nullable=False)
    start = db.Column(db.Time, nullable=False)
    end = db.Column(db.Time, nullable=False)
    accepted = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, user_id, bookable_id, date, start, end, accepted=True):
        self.user_id = user_id
        self.bookable_id = bookable_id
        self.date = date
        self.start = start
        self.end = end
        self.accepted = accepted

    def serialize(self):
        return {
            "user_id": self.user_id,
            "bookable_id": self.bookable_id,
            "date": json_serial_date(self.date),
            "start": str(self.start),
            "end": str(self.end),
        }
