from flask_restful import Resource
from model import Rooms


class GetRooms(Resource):

    def get(self):
        return Rooms.query.all()

    def post(self):
        return 'OK'

    def delete(self):
        return 'OK'

