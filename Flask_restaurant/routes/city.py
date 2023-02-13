import json
from flask import request, Blueprint, Response
from flask_restful import Resource
from infrastructure import DB
from model import City

cities_bp = Blueprint('GetCities', __name__)

class GetCity(Resource):
    def get(self):
        city = [{"id_city": city.id_city, "name": city.name} for city in DB['city']]
        js_data = json.dumps(city)
        return Response(js_data, status=200)



    def post(self):
        data = request.json
        if len(DB['city']) == 0:
            DB['city'].append(City(data['name']))
        else:
            for city in DB['city']:
                if city.name == data['name']:
                    return "This city is already in list"
                else:
                    DB['city'].append(City(data['name']))
                    city = [{"id_city": city.id_city, "name": city.name} for city in DB['city']]
                    js_data = json.dumps(city)
                    return Response(js_data, status=200)
        city = [{"id_city": city.id_city, "name": city.name} for city in DB['city']]
        js_data = json.dumps(city)
        return Response(js_data, status=200)

    def delete(self, id_city):
        DB['city'] = [city for city in DB['city'] if city.id_city != id_city]
        return Response(status=200)



