from flask_restful import Resource, Api
from flask import request, make_response, jsonify, abort
from . import application
from app import logging
from models import PerformanceAnalysis, PerformanceAnalysisSchema, DeviceManagement, DeviceManagementSchema
from validation import BarQuerySchema, SearchSchema
from db_config import db

application_api = Api(application)

schema = BarQuerySchema()
schema_search = SearchSchema()


# @application_api.resource('/')
class DeviceManagementEngine(Resource):
    def get(self):
        #  here we will get last 24 hr data by default
        device_data = DeviceManagement.query.all()
        # Serialize the data for the response
        device_management_schema = DeviceManagementSchema(many=True)
        result = device_management_schema.dump(device_data)
        print(result)
        if not result:
            return jsonify({'msg': 'No record Found'})
        logging.info("Result")
        logging.info(result)
        # return make_response(jsonify({"data": result}, 200))
        return jsonify(result)

    def post(self):
        return make_response(jsonify({"msg": "POSt"}))

    def put(self):
        id = request.json['id']
        logging.info("Id")
        logging.info(id)
        rec = DeviceManagement.query.filter_by(id=id).first()
        if rec:
            rec.probe_name = request.json['probe_name']
            rec.region = request.json['region']
            rec.site_name = request.json['site_name']
            rec.mobile_technology = request.json['mobile_technology']
            rec.mobile_model = request.json['mobile_model']
            rec.cordinates = request.json['cordinates']
            rec.date_of_installation = request.json['date_of_installation']
            rec.device_id = request.json['device_id']
            rec.mobile_number = request.json['mobile_number']
            rec.mobile_os = request.json['mobile_os']
            rec.current_version = request.json['current_version']
            rec.update = request.json['update']
            rec.remote_management = request.json['remote_management']
            db.session.commit()
            return make_response({"msg": "Record has been updated"}, 202)
        else:
            return make_response({"msg": "Record does not exist"}, 404)


class DeviceManagementUpdate(Resource):
    def get(self):
        return {"msg": "Success"}

    def put(self):
        id = request.json['id']
        logging.info("Id")
        logging.info(id)
        rec = DeviceManagement.query.filter_by(id=id).first()
        current_version = float(rec.current_version)
        present_version = float(rec.update.split()[-1])
        if current_version < present_version:
            print("Run the ssh command and check for new update")
            if rec:
                rec.update = request.json['update']
                db.session.commit()
                return make_response({"msg": "Record has been updated"}, 202)
            else:
                return make_response({"msg": "Record does not exist"}, 404)
        else:
            pass


class DeviceManagementRemoteAccessApi(Resource):
    def get(self):
        errors = schema.validate(request.args)
        print(errors)
        if errors:
            abort(400, str(errors))

        id = request.args.get('id')
        rec = DeviceManagement.query.filter_by(id=id)
        device_management_schema = DeviceManagementSchema(many=True)
        result = device_management_schema.dump(rec)
        if result:
            return make_response({"status": True, "data": result})
        else:
            return make_response({"status": False, "data": []})


class SearchApi(Resource):

    def get(self):
        global query_dict
        errors = schema_search.validate(request.args)
        if errors:
            abort(400, str(errors))

        device_management_type = request.args.get('type')
        probe = request.args.get('probe')
        region = request.args.get('region')
        site_name = request.args.get('site_name')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')

        if probe and region and site_name and start_date and end_date:
            query_dict = {"probe": probe, "region": region, "site_name": site_name, "start_date": start_date,
                          "end_date": end_date, "app_type": device_management_type}

        if probe and region and site_name:
            query_dict = {"probe": probe, "region": region, "site_name": site_name, "app_type": device_management_type}

        if probe and region:
            query_dict = {"probe": probe, "region": region, "app_type": device_management_type}

        if probe:
            query_dict = {"probe": probe, "app_type": device_management_type}

        if probe and site_name:
            query_dict = {"probe": probe, "site_name": site_name, "app_type": device_management_type}

        results = PerformanceAnalysis.query.filter_by(**query_dict).all()
        device_management_schema = PerformanceAnalysisSchema(many=True)
        result = device_management_schema.dump(results)

        if result:
            return {"status": True, "msg": result}
        else:
            return {"status": False, "msg": "No Data Found"}

# application_api.add_resource(DeviceManagementEngine, '/application')
# application_api.add_resource(SearchApi, '/search')
