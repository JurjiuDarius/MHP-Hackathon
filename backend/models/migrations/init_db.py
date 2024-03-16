from models.room import Room
from models.desk import Desk
from models.user import User

from database import db

ROOMS_LOCATION = "models/migrations/extracted_rooms.txt"
DESKS_LOCATION = "models/migrations/extracted_desks.txt"


def add_rooms_to_database():
    with open(ROOMS_LOCATION, "r") as file:
        for line in file:
            split_info = id = line.split(" ")
            id = split_info[0]
            capacity = int(split_info[3])
            room = Room(id=id, capacity=capacity)
            db.session.add(room)
            db.session.commit()
