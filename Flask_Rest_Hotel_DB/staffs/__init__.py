from flask import Blueprint
from flask_restful import Api
from staffs.routes import GetStaff

staff_bp = Blueprint("staff", __name__)
api_staff = Api(staff_bp)
api_staff.add_resource(GetStaff, '/staff')

