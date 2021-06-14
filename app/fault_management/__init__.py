from flask import Blueprint
from flask_restful import Api

fm = Blueprint("fm_view", __name__, url_prefix="/pms/fm")

from .fm import *

fm_api.add_resource(FmEngine, '/')
