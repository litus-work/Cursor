from flask import Blueprint
from flask_restful import Api
from rooms.routes import GetRooms

rooms_bp = Blueprint("rooms", __name__)
api_rooms = Api(rooms_bp)
api_rooms.add_resource(GetRooms, '/rooms')

