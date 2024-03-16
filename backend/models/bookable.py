from database import db
from sqlalchemy.orm import Mapped, mapped_column


class Bookable(db.Model):
    id = id = mapped_column(db.String, primary_key=True)
    map_id = db.Column(db.Integer, nullable=False, unique=True)
    bookings = db.relationship("Booking", back_populates="bookable", lazy=True)
    type: Mapped[str]

    __mapper_args__ = {
        "polymorphic_identity": "bookable",
        "polymorphic_on": "type",
    }

    def __init__(self, map_id):
        self.map_id = map_id
