from datetime import timedelta
from flask import Flask
from config import run_config
from db import db
from flask_restful import Api
from rooms.routes import GetRoom, AddStaff
from tenants.routes import GetTenants
from staff.routes import GetStaff
from tenants import tenant_bp
from staff import staff_bp
from rooms import room_bp



def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(run_config())

    db.init_app(app)
    app.permanent_session_lifetime = timedelta(minutes=20)  # add session expire time

    api = Api(app)
    api.add_resource(GetRoom, '/rooms')
    api.add_resource(GetTenants, '/tenants')
    api.add_resource(GetStaff, '/staff')
    api.add_resource(AddStaff, '/add_staff')


    with app.app_context():
        app.register_blueprint(room_bp)
        app.register_blueprint(tenant_bp)
        app.register_blueprint(staff_bp)
        db.create_all()
        db.session.commit()


        return app


app = create_app()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
