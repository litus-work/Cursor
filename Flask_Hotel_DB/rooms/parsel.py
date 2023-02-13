from flask_restful import reqparse

room_parser = reqparse.RequestParser()
room_parser.add_argument("name", required=True, help="Important: {error_msg}!!!")