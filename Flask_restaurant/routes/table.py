import json
from flask import Response, request, Blueprint
from flask_restful import Resource, marshal_with, fields, reqparse
from infrastructure import DB
from model import Table

tables_bp = Blueprint('table', __name__)
get_table_id_fields = {
    "id_table": fields.String,
    "number": fields.Integer,
    "guest_count": fields.Integer,
    "rest_name": fields.String
}

pars_table = reqparse.RequestParser()
pars_table.add_argument('id_table', type=str)

class GetTables(Resource):
    def get(self):
        resp = [{"id_table": resp.id_table, "number": resp.number, "guest_count": resp.guest_count, "rest_name": resp.rest_name} for resp in DB['table']]
        js_data = json.dumps(resp)
        return Response(js_data, status=200)

    def post(self):
        data = json.loads(request.data)
        # data = request.json
        for tables in DB['table']:
            if data['number'] != tables.number:
                for rest in DB['restaurant']:
                    if data['rest_name'] == rest.name:
                            DB['table'].append(Table(data['number'], data['guest_count'], data['rest_name'], data['user']))
        table = [{"id_table": table.id_table, "number": table.number, "guest_count": table.guest_count, "rest_name": table.rest_name, "user": table.user} for table in DB['table']]
        js_data = json.dumps(table)
        return Response(js_data, status=200)

    def delete(self, id_table):
        DB['table'] = [x for x in DB['table'] if x.id_table != id_table]
        resp = [{"id_table": resp.id_table, "number": resp.number, "guest_count": resp.guest_count} for resp in DB['table']]
        js_data = json.dumps(resp)
        return Response(js_data, status=200)


class GetTableByID(Resource):
    @marshal_with(get_table_id_fields)
    def get(self, id_table):
        print(id_table)
        print(pars_table.parse_args())
        print(pars_table.parse_args().get('id_table'))
        if pars_table.parse_args().get('id_table'):
            for tables in DB['table']:
                print(tables)
                print(tables.id_table)
                if tables.id_table == id_table:
                    print('1=1')
                    resp = {"id_table": tables.id_table, "number": tables.number, "guest_count": tables.guest_count, "rest_name": tables.rest_name}
                    return resp
        else:
            return 'All tables'
