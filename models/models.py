from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(50), nullable=False)
    asin = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    source = db.Column(db.String(100), nullable=False)
    stars = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Event {self.id}>'
