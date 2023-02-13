import json

from flask import Blueprint, request, Response
from flask_restful import Resource

from infrastructure import DB
from model import Restaurant

restaurants_bp = Blueprint('restaurant', __name__)


class GetRest(Resource):
    def get(self):
        rest = [{"id_rest": rest.id_rest, "name": rest.name, "stars": rest.stars, "city": rest.city} for rest in DB['restaurant']]
        js_data = json.dumps(rest)
        return Response(js_data, status=200)

    def post(self):
        data = request.json
        if len(DB['restaurant']) == 0:
            [(DB['restaurant'].append(Restaurant(data['name'], data['stars'], data['city']))) for x in DB['city'] if data['city'] == x.name]
            rest = [{"id_rest": rest.id_rest, "name": rest.name, "stars": rest.stars, "city": rest.city} for rest in DB['restaurant']]
            js_data = json.dumps(rest)
            return Response(js_data, status=200)
        else:
            for rest in DB['restaurant']:
                [(DB['restaurant'].append(Restaurant(data['name'], data['stars'], data['city']))) for x in DB['city'] if data['city'] == x.name if rest.name != data['name']]
            rest = [{"id_rest": rest.id_rest, "name": rest.name, "stars": rest.stars, "city": rest.city} for rest in DB['restaurant']]
            js_data = json.dumps(rest)
            return Response(js_data, status=200)













                # for city in DB['city']:
                #     while data['city'] == city.name:
                #         DB['restaurant'].append(Restaurant(data['name'], data['stars'], data['city']))
                #     else:
                #         return "You can't create restaurant in non-existent city"
        # else:
        #     for rest in DB['restaurant']:
        #         print(rest.name)
        #         print(data)
        #         print(data['name'])
        #         if rest.name == data['name']:
        #             return "This restaurant is already in list"
        #         else:
        #             for city in DB['city']:
        #                 if data['city'] == city.name:
        #                     DB['restaurant'].append(Restaurant(data['name'], data['stars'], data['city']))
        #                 else:
        #                     return "You can't create restaurant in non-existent city"
        #
        # rest = [{"id_rest": rest.id_rest, "name": rest.name, "stars": rest.stars, "city": rest.city} for rest in DB['restaurant']]
        # js_data = json.dumps(rest)
        # return Response(js_data, status=200)





    def delete(self, id_rest):
        DB['restaurant'] = [x for x in DB['restaurant'] if x.id_rest != id_rest]
        rest = [{"id_rest": rest.id_rest, "name": rest.name, "stars": rest.stars} for rest in DB['restaurant']]
        js_data = json.dumps(rest)
        return Response(js_data, status=200)
