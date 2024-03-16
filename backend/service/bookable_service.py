from models import Room, Desk
from database import db


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
