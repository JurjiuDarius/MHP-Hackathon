from models.room import Room
from models.desk import Desk
from models.user import User

from database import db

ROOMS_LOCATION = "models/migrations/extracted_rooms.txt"
DESKS_LOCATION = "models/migrations/extracted_desks.txt"
MAP_ID = "5th Floor"
USER_LOCATION = "models/migrations/mock_users.txt"


def add_rooms_to_database():
    with open(ROOMS_LOCATION, "r") as file:
        for line in file:
            split_info = id = line.strip().split(" ")
            if "" in split_info:
                split_info.remove(" ")
            id = split_info[0]
            capacity = int(split_info[3])
            room = Room.query.get(id)
            if not room:
                room = Room(id=id, map_id=MAP_ID, capacity=capacity)
                db.session.add(room)
                db.session.commit()


def add_desks_to_database():
    with open(DESKS_LOCATION, "r") as file:
        for line in file:
            split_info = id = line.strip().split(" ")
            id = split_info[0]
            if "" in split_info:
                split_info.remove("")
            desk = Desk.query.get(id)
            if not desk:
                desk = Desk(id=id, map_id=MAP_ID)
                db.session.add(desk)
                db.session.commit()


def add_users_to_database():
    with open(USER_LOCATION, "r") as file:
        for line in file:
            split_info = line.strip().split(" ")
            if "" in split_info:
                split_info.remove("")
            email = split_info[0]
            password = split_info[1]
            username = split_info[2]
            role = split_info[3]

            user = User.query.filter_by(email=email).first()
            if not user:
                user = User(
                    email=email,
                    username=username,
                    password=password,
                    role=role,
                )
                db.session.add(user)
                db.session.commit()


def add_all_to_database():
    add_rooms_to_database()
    add_desks_to_database()
    add_users_to_database()
