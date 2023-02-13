from flask import json, request
from flask_restful import Resource, marshal_with, fields

from db import db
from model import RoomModel, StaffModel

staff_structure = {
    "staff_id": fields.Integer
}

room_structure = {
    "number": fields.Integer,
    "level": fields.Integer,
    "status": fields.String,
    "price": fields.Integer,
    "tenant_id": fields.Integer,
    "staff": fields.Nested(staff_structure)
}

# room_staff_structure = {
#     "staff_id": fields.Integer
# }

class GetRoom(Resource):

    @marshal_with(room_structure)
    def get(self):
        return RoomModel.query.all()

    def post(self):
        data = json.loads(request.data)
        new_room = RoomModel(**data)
        db.session.add(new_room)
        db.session.commit()
        return "Successfully added a new news"

class AddStaff(Resource):
    @marshal_with(room_structure)
    def get(self):
        return RoomModel.query.all()

    def post(self):
        data = json.loads(request.data)
        room_number = data.get("room_number")
        new_staff_id = data.get("staff_id")
        room = RoomModel.query.filter_by(number=room_number).first()
        new_staff = StaffModel.query.filter_by(passport_id=new_staff_id).first()
        room.staff.append(new_staff)
        db.session.commit()
        return f"Successfully added a new staff {new_staff.passport_id} to room {room.number}"



