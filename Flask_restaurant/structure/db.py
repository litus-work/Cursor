from flask import Flask
from flask_sqlalchemy import SQLAlchemy

PG_USER = 'litus_cursor'
PG_PASSWORD = '0791LitusCursor'
PG_HOST = '127.0.0.1'
PG_PORT = 5432
DB_NAME = 'cursor_bd'

SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)


class CityTable(db.Model):
    __tablename__ = 'city_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cityname = db.Column(db.String(80), unique=True, nullable=False)
    country = db.Column(db.String(80), unique=True, nullable=False)
    users = db.relationship('UserTable', backref='city')

class UserTable(db.Model):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    cityname = db.Column(db.String(80), db.ForeignKey('city_table.id'))

    def __repr__(self):
        return '<User %r>' % self.username


app.app_context().push()
db.create_all()
db.session.commit()

if __name__ == '__main__':
    app.run()
