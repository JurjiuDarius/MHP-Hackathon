from database import db


class Desk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookable_id = db.Column(db.Integer, db.ForeignKey('bookable.id'), nullable=False)
