from datetime import datetime
from my_website import db


class GameUserAssociation(db.model):
    __table__ = "game_user"
    game_id = db.Column(db.Integer, db.ForeignKey())
    user_id = db.Column(db.Integer, db.ForeignKey())
    score = db.Column(db.Integer)


class Game(db.Model):
    __table__ = "game"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    winner_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model):
    __table__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
