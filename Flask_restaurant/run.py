from flask import Flask
from infrastructure import DB
from routes.city import GetCity, cities_bp
from routes.restaurant import GetRest, restaurants_bp
from routes.table import tables_bp, GetTables, GetTableByID
from flask_restful import Api


def setup_db():
    DB['restaurant'] = []
    DB['table'] = []
    DB['city'] = []


def create_app():
    setup_db()
    app = Flask(__name__, instance_relative_config=False)
    api = Api(app)
    api.add_resource(GetCity, '/city', '/city/<string:id_city>')
    api.add_resource(GetRest, '/restaurant', '/restaurant/<string:id_rest>')
    api.add_resource(GetTableByID, '/table/<string:id_table>')
    api.add_resource(GetTables, '/table')

    with app.app_context():
        app.register_blueprint(restaurants_bp)
        app.register_blueprint(tables_bp)
        app.register_blueprint(cities_bp)
        return app


app = create_app()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
