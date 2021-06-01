from flask import Blueprint
from flask_restful import Api

fm = Blueprint("fm_view", __name__, url_prefix="/pms/fm")
# fm_api = Api(fm)

from .fm import *
