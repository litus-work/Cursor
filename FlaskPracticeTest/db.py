from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

studios_films = db.Table(
    'studios_films',
    db.Column('studio_id', db.Integer, db.ForeignKey('studios.id')),
    db.Column('film_id', db.Integer, db.ForeignKey('films.id'))
)


class Films(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    year = db.Column(db.Integer)
    # studio = db.relationship('Studios', secondary=studios_films, backref='film')

class Studios(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    films = db.relationship('Films', secondary=studios_films, backref='studio')

