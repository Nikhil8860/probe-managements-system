from flask import Blueprint
from flask_restful import Api

pa = Blueprint("pa_view", __name__, url_prefix="/pms/pa")
pa_api = Api(pa)

from .application import *

pa_api.add_resource(PaEngine, '/')
pa_api.add_resource(SearchApiApplication, '/performance-analysis-application/application')
pa_api.add_resource(SearchApiNetwork, '/performance-analysis-application/network')
pa_api.add_resource(SearchApiWebService, '/performance-analysis-application/webservice')
