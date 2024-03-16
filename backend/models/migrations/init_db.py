from database import db
from models.room import Room

ROOMS_FILE = "models/extracted_rooms.csv"


def add_rooms():

    with open(ROOMS_FILE, "r") as file:
        lines = file.readlines()
        for line in lines:
            room = line.split(",")
            room = Room(
                room_type_id=room[0],
                room_status_id=room[1],
                room_number=room[2],
            )
            db.session.add(room)

    room_types = RoomType.query.all()
    room_statuses = RoomStatus.query.all()

    for room_type in room_types:
        for room_status in room_statuses:
            room = Room(
                room_type_id=room_type.id,
                room_status_id=room_status.id,
                room_number=f"{room_type.id}{room_status.id}",
            )
            db.session.add(room)
    db.session.commit()
