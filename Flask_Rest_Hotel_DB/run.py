from datetime import timedelta
from config import run_config
from db import db
from rooms import rooms_bp, staffs_bp, tenants_bp
from flask import Flask

from staffs import staff_bp
from tenants import tenant_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())
    db.init_app(app)
    app.permanent_session_lifetime = timedelta(minutes=20)
    app.register_blueprint(rooms_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(tenant_bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
