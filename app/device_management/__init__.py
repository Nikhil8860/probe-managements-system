from flask import Blueprint

application = Blueprint("dm_view", __name__, url_prefix="/pms/dm/v1.0")

from .application import *
application_api.add_resource(DeviceManagementEngine, '/application')
application_api.add_resource(SearchApi, '/search')
application_api.add_resource(DeviceManagementUpdate, '/application/update')
application_api.add_resource(DeviceManagementRemoteAccessApi, '/application/remote-access')
application_api.add_resource(OpenTerminal, '/application/terminal')
