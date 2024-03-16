from database import db
from models import Booking, User, Room
from datetime import datetime, timedelta
from sqlalchemy import and_
from utils.date import mdy_to_dmy, is_date


def create_booking(user_id, bookable_id, date, start, end, people):
    date = mdy_to_dmy(date)
    if is_date(date, date_format="%m/%d/%Y") is False:
        return "Invalid date", 400
    if start > end:
        return "Invalid time", 400
    if len(people) > 0:
        room = Room.query.get(bookable_id)
        if not room:
            return "Room not found", 404
        if len(people) + 1 > room.capacity:
            return "Too many people for the room", 400
        if len(people) + 1 < room.capacity / 2:
            return "Too few people for the room", 400

    booking = Booking(
        user_id=user_id, bookable_id=bookable_id, date=date, start=start, end=end
    )
    db.session.add(booking)

    for email in people:
        user = User.query.filter_by(email=email).first()
        if user:
            booking = Booking(
                user_id=user.id,
                bookable_id=bookable_id,
                date=date,
                start=start,
                end=end,
                accepted=False,
            )
            db.session.add(booking)
    db.session.commit()
    return booking


def get_booking(booking_id):
    return Booking.query.get(booking_id)


def update_booking(booking_id, date=None, start=None, end=None, room_id=None):
    booking = Booking.query.get(booking_id)
    if date:
        date = mdy_to_dmy(date)
        if is_date(date, date_format="%m/%d/%Y") is False:
            return "Invalid date", 400
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
    date = mdy_to_dmy(date)
    if is_date(date, date_format="%m/%d/%Y") is False:
        return "Invalid date", 400

    filtered_bookings = Booking.query.filter_by(date=date).all()
    return [booking.serialize() for booking in filtered_bookings]


def get_all_bookings():
    return [booking.serialize() for booking in Booking.query.all()]


def get_current_bookings_for_user(user_id):
    # checkk if user exists
    user = User.query.get(user_id)
    if not user:
        return {"message": "User not found!"}, 404
    current_bookings = Booking.query.filter(
        and_(
            Booking.user_id == user_id,
            Booking.date > (datetime.now() - timedelta(1)).date(),
        ),
    ).all()
    return [booking.serialize() for booking in current_bookings], 200


def get_past_bookings_for_user(user_id):
    # checkk if user exists
    user = User.query.get(user_id)
    if not user:
        return {"message": "User not found!"}, 404
    past_bookings = Booking.query.filter(
        and_(
            Booking.date < datetime.now().date(),
            Booking.user_id == user_id,
        )
    ).all()
    return [booking.serialize() for booking in past_bookings], 200
