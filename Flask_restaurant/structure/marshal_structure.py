from flask_restful import fields

#
# city_fields = {'room_id': fields.Integer,
#                'number': fields.Integer,
#                'level': fields.String,
#                'status': fields.String,
#                'price': fields.Integer,
#                'tenant_id': fields.Integer}

city_fields = {'id_city': fields.Integer,
               'name': fields.String}

