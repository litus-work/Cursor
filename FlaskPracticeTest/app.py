from flask import Flask
from api.films import films_blueprint
from api.studios import studios_blueprint
from config import get_config
from db import db


def create_app(env="DEV"):
    app = Flask(__name__)
    app.config.from_object(get_config(env))
    db.init_app(app)
    app.register_blueprint(films_blueprint)
    app.register_blueprint(studios_blueprint)

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
