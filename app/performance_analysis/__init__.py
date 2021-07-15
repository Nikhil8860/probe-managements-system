from flask import Blueprint
from flask_restful import Api

pa = Blueprint("pa_view", __name__, url_prefix="/pms/pa/v1.0")
pa_api = Api(pa)

from .application import *

pa_api.add_resource(PaEngine, '/')
pa_api.add_resource(SearchApiApplication, '/performance-analysis-application/application')
pa_api.add_resource(SearchApiNetwork, '/performance-analysis-application/network')
pa_api.add_resource(SearchApiWebService, '/performance-analysis-application/webservice')
pa_api.add_resource(SearchApiProbe, '/performance-analysis-application/application/probe-search')
pa_api.add_resource(GetProbe, '/probe/get-probe-name')
pa_api.add_resource(GetNetwork, '/probe/get-network-name')
pa_api.add_resource(GetWebServices, '/probe/get-web-services-name')
