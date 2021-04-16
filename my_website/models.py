from datetime import datetime
from my_website import db


class User(db.Model):
    __tablename__ = "user"
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    num_games_played = db.Column(db.Integer, nullable=False, default=0)
    game_won = db.relationship("Game", backref="winner")
    player_score = db.relationship("Score", backref="player")

    def __repr__(self):
        return f"User({self.name}, {self.num_games_played})"


class Game(db.Model):
    __tablename__ = "game"
    id_ = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    winner_id = db.Column(db.Integer, db.ForeignKey("user.id_"), nullable=True)
    game_score = db.relationship("Score", backref="game")

    def __repr__(self):
        return f"Game({self.date}, {self.winner_id})"


class Score(db.Model):
    __tablename__ = "score"
    id_ = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id_"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id_"), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Score({self.game_id}, {self.user_id}, {self.score})"
