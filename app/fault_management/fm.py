from re import I
from flask_restful import Api, Resource
from flask import jsonify, current_app, make_response, abort, request
import logging
from . import fm
from models.fault_management import fault_model
from device_health import cpu_memory_stastics_alert
from validation import BarQuerySchema
from models.fault_management import fault_model
from db_config import db

schema = BarQuerySchema()
logger = logging.getLogger(__name__)

fm_api = Api(fm)

oids_dict = {
    "cpu": [".1.3.6.1.4.1.2021.11.10.0"],
    "memory": ['.1.3.6.1.4.1.2021.4.6.0', '.1.3.6.1.4.1.2021.4.11.0'],
}


class FmEngine(Resource):
    def get(self):
        fault_description = cpu_memory_stastics_alert.get_data_from_oids(oids_dict)
        print(fault_description)
        current_app.logger.info("Fault Management Started Get Request")
        data = fault_model.FaultManagement.query.all()
        fault_management_schema = fault_model.FaultManagementSchema(many=True)
        result = fault_management_schema.dump(data)
        if not result:
            return jsonify({"status": True, 'msg': 'No record Found'})
        current_app.logger.info("Result")
        current_app.logger.info(result)
        return make_response(jsonify({"status": True, "data": result}, 200))

    def put(self):
        #  This API is for comment
        errors = schema.validate(request.args)
        if errors:
            abort(400, str(errors))
        id = request.args.get('id')
        comment = request.form['comment']
        print(comment)
        current_app.logger.info("Comment")
        current_app.logger.info(comment)
        fault_data = fault_model.FaultManagement.query.filter_by(fault_id=id).first()
        if fault_data:
            fault_data.comment = comment
            db.session.commit()
            return make_response({"status": True, "msg":"Comment inserted"}, 202)
        else:
            return make_response({"status": False, "msg": "Record does not exist"}, 404)
