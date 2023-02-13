from flask import json, request
from flask_restful import Resource, fields, marshal_with

from db import db
from model import TenantModel

rooms_structure = {
    "number": fields.Integer
}

tenant_structure = {
    "passport_id": fields.Integer,
    "name": fields.String,
    "age": fields.Integer,
    "sex": fields.String,
    "address": fields.String,
    "rooms": fields.Nested(rooms_structure)
}

class GetTenants(Resource):
    @marshal_with(tenant_structure)
    def get(self):
        return TenantModel.query.all()



    def post(self):
        data = json.loads(request.data)
        new_tenant = TenantModel(**data)
        db.session.add(new_tenant)
        db.session.commit()
        return "OK"