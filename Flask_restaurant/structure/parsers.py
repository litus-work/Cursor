from flask_restful import reqparse


pars_city = reqparse.RequestParser()
pars_city.add_argument('id_city', type=int)

