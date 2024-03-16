from database import db
from models import Booking


def create_booking(user_id, bookable_id, date, start, end):
    booking = Booking(
        user_id=user_id, bookable_id=bookable_id, date=date, start=start, end=end
    )
    db.session.add(booking)
    db.session.commit()
    return booking


def get_booking(booking_id):
    return Booking.query.get(booking_id)


def update_booking(booking_id, date=None, start=None, end=None, room_id=None):
    booking = Booking.query.get(booking_id)
    if date:
        booking.date = date
    if start:
        booking.start = start
    if end:
        booking.end = end
    if room_id:
        booking.room_id = room_id
    db.session.commit()
    return booking


def delete_booking(booking_id):
    booking = Booking.query.get(booking_id)
    db.session.delete(booking)
    db.session.commit()


def filter_bookings_by_date(date):
    return Booking.query.filter_by(date=date).all()
