from database import db
from models.bookable import Bookable
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


class Desk(Bookable):
    id = db.Column(db.String, db.ForeignKey("bookable.id"), primary_key=True)

    number_available = db.Column(db.Integer, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "desk",
    }

    def __init__(self, number_available):
        self.number_available = number_available
