from database import db
from models import User


def get_users():
    users = User.query.all()
    return [user.serialize() for user in users]
