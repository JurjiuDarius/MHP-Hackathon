from models import Room, Desk
from database import db
from utils.date import mdy_to_dmy
import numpy as np

from ai_component.ai_interactive_logic import ai_controller


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
    date = mdy_to_dmy(date)
    ai = ai_controller()
    morning_availability = ai.get_desk_prediction_morning(bookable_id, date)
    evening_availability = ai.get_desk_prediction_evening(bookable_id, date)

    morning_availability = "{:.2f}".format(morning_availability)
    evening_availability = "{:.2f}".format(evening_availability)
    return [morning_availability, evening_availability], 200
