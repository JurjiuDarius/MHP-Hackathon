from database import db
from sqlalchemy.orm import mapped_column

class User(db.Model):
    id = mapped_column(db.Integer, primary_key=True, autoincrement=True)

