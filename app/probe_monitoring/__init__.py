from flask import Blueprint
from flask_restful import Api

pm = Blueprint("pm_view", __name__, url_prefix="/pms/pm/v1.0")
# pm_api = Api(pm)

from .pm import *
