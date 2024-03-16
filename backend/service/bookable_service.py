from models import Room, Desk, Bookable, Booking
from database import db
from utils.date import mdy_to_dmy, is_date
from ai_component.ai_interactive_logic import ai_controller
import datetime


def get_bookable_capacity(bookable_id):
    room = Room.query.get(bookable_id)
    if room:
        return room.capacity, 200
    else:
        desk = Desk.query.get(bookable_id)
        if desk:
            return 1, 200
        else:
            return "Room or desk not found", 404


def get_bookable_availability(data):
    bookable_id = data["bookableId"]
    date = data["date"]
    if (
        is_date(
            date,
        )
        is False
    ):
        return "Invalid date", 400
    date = mdy_to_dmy(date)
    date_object = datetime.datetime.strptime(date, "%d/%m/%Y")
    day_of_week_numeric = date_object.weekday()
    if day_of_week_numeric > 4:
        return "The date is not a weekday", 400

    ai = ai_controller()
    morning_availability = ai.get_desk_prediction_morning(bookable_id, date)
    evening_availability = ai.get_desk_prediction_evening(bookable_id, date)

    morning_availability = "{:.2f}".format(morning_availability)
    evening_availability = "{:.2f}".format(evening_availability)
    return [morning_availability, evening_availability], 200


def get_bookable_colors(data):
    """Check if a room has no occupation, is partially occupied or fully occupied"""
    date = data["date"]
    date = mdy_to_dmy(date)
    if (
        is_date(
            date,
        )
        is False
    ):
        return "Invalid date", 400
    bookables = Bookable.query.all()
    color_dictionary = {}
    for bookable in bookables:
        bookings = Booking.query.filter_by(bookable_id=bookable.id, date=date).all()
        min_start = datetime.time(17, 0)
        max_end = datetime.time(9, 0)
        if len(bookings) == 0:
            color_dictionary[bookable.id] = 0
            continue
        for booking in bookings:
            current_start = booking.start
            current_end = booking.end
            min_start = min(min_start, current_start)
            max_end = max(max_end, current_end)
        if min_start < datetime.time(9, 0) and max_end > datetime.time(17, 0):
            color_dictionary[bookable.id] = 2
        else:
            color_dictionary[bookable.id] = 1

    return color_dictionary, 200
