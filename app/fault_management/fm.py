from flask_restful import Api, Resource
import logging
from . import fm

fm_api = Api(fm)

logger = logging.getLogger(__name__)


class FmEngine(Resource):
    def get(self):
        logger.info("Fault Management Started Get Request")
        return {"msg": "Success from FM"}

    def post(self):
        # print(request.json())
        return {"msg": "POST"}


fm_api.add_resource(FmEngine, '/')
