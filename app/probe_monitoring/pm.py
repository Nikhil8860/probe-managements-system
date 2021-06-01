from flask_restful import Api, Resource
import logging
from . import pm

fm_api = Api(pm)

logger = logging.getLogger(__name__)


class PmEngine(Resource):
    def get(self):
        logger.info("Probe Monitoring Started Get Request")
        return {"msg": "Success from PM"}

    def post(self):
        # print(request.json())
        return {"msg": "POST"}


fm_api.add_resource(PmEngine, '/')
