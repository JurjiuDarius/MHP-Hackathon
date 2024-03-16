from database import db
from models.bookable import Bookable
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


class Room(Bookable):
    id = db.Column(db.String, db.ForeignKey("bookable.id"), primary_key=True)

    capacity = db.Column(db.Integer, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "room",
    }

    def __init__(self, id, map_id, capacity):
        super().__init__(map_id)
        self.id = id
        self.capacity = capacity
