from database import db
from models.bookable import Bookable
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


class Room(Bookable):
    id = db.Column(db.String, db.ForeignKey("bookable.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "room",
    }
