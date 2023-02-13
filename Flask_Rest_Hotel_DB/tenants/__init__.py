from flask import Blueprint
from flask_restful import Api
from tenants.routes import GetTenant

tenant_bp = Blueprint("tenant", __name__)
api_tenant = Api(tenant_bp)
api_tenant.add_resource(GetTenant, '/tenant')

