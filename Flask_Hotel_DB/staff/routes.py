from flask import json, request
from flask_restful import Resource, fields, marshal_with

from db import db
from model import StaffModel

staff_structure = {
    "passport_id": fields.Integer,
    "name": fields.String,
    "position": fields.String,
    "salary": fields.Integer
}

class GetStaff(Resource):
    @marshal_with(staff_structure)
    def get(self):
        return StaffModel.query.all()


    def post(self):
        data = json.loads(request.data)
        new_staff = StaffModel(**data)
        db.session.add(new_staff)
        db.session.commit()
        return "Successfully added a new news"