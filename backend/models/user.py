from sqlalchemy import Enum
from database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    role = db.Column(Enum("admin", "employee", name="user_role_enum"), nullable=False)

    bookings = db.relationship("Booking", back_populates="user", lazy=True)

    def __init__(self, email, password, username, role):
        self.email = email
        self.password = password
        self.username = username
        self.role = role
