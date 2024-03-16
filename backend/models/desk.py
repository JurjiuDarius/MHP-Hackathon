from database import db
from models.bookable import Bookable
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


class Desk(Bookable):
    id = db.Column(db.String, db.ForeignKey("bookable.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "desk",
    }

    def __init__(self, id, map_id):
        super().__init__(map_id)
        self.id = id
        self.map_id = map_id
