from flask_restful import Resource
from flask import request, make_response, abort, jsonify
from db_config import db
from validation import BarQuerySchema, SearchSchema
from models import PerformanceAnalysis, PerformanceAnalysisSchema
from app import logging
import datetime

schema = BarQuerySchema()
schema_search = SearchSchema()


class PaEngine(Resource):
    list_data = []

    def get(self):
        return {"msg": PaEngine.list_data}

    def post(self):
        if type(request.json['values']) == list:
            for i in request.json['values']:
                PaEngine.list_data.append(i)
        else:
            PaEngine.list_data.append(request.json['values'])
        return make_response({"msg": "Post Success from PA"}, 201)

    def put(self):
        PaEngine.list_data[0] = 10
        return make_response({"msg": "PUT"}, 202)

    def delete(self):
        if PaEngine.list_data:
            PaEngine.list_data.pop()
        else:
            return make_response({"msg": "No Data Exists"}, 404)
        return make_response({"msg": "DELETE"}, 202)


class SearchApiApplication(Resource):

    def __init__(self):
        self.device_management_type = request.args.get('type')
        self.probe = request.args.get('probe')
        self.region = request.args.get('region')
        self.site_name = request.args.get('site_name')
        self.start_date = request.args.get('start_date')
        self.end_date = request.args.get('end_date')
        self.query_dict = dict()

    def get(self):
        errors = schema_search.validate(request.args)
        if errors:
            abort(400, str(errors))
        if not self.probe and not self.site_name and not self.start_date and not self.end_date:
            # self.query_dict = {"app_type": self.device_management_type}
            self.query_dict = {}
        if self.probe and self.region and self.site_name and self.start_date and self.end_date and self.device_management_type:
            self.query_dict = {"probe": self.probe, "region": self.region, "site_name": self.site_name,
                               "start_date": self.start_date,
                               "end_date": self.end_date, "app_type": self.device_management_type}
        else:
            pass

        print(self.query_dict)
        results = PerformanceAnalysis.query.filter_by(**self.query_dict).all()
        performance_analysis = PerformanceAnalysisSchema(many=True)
        result = performance_analysis.dump(results)

        if result:
            return {"status": True, "data": result}
        else:
            return {"status": False, "data": "No Data Found"}

    def post(self):
        probe = request.json['probe']
        logging.info("Probe from request" + str(probe))
        test = PerformanceAnalysis.query.filter_by(probe=probe).first()
        if test:
            return make_response(jsonify({'msg': "Result already exists"}, 409))
        else:
            start_date = datetime.datetime.strptime(request.json['start_date'], '%d/%m/%Y')
            end_date = datetime.datetime.strptime(request.json['end_date'], '%d/%m/%Y')
            region = request.json['region']
            site_name = request.json['site_name']
            probe = request.json['probe']
            app_type = request.json['app_type']
            p = PerformanceAnalysis(start_date=start_date, end_date=end_date, region=region, site_name=site_name,
                                    probe=probe, app_type=app_type)
            db.session.add(p)
            db.session.commit()
            return make_response({"msg": "Data has been Inserted"}, 201)

    def delete(self):
        id = request.args.get('id')
        rec = PerformanceAnalysis.query.filter_by(id=id).first()
        if rec:
            db.session.delete(rec)
            db.session.commit()
            return make_response({"msg": "Record has been Deleted"}, 202)
        else:
            return make_response({'msg': "Record does not exist"}, 404)


class SearchApiNetwork(SearchApiApplication):
    def __init__(self):
        super(SearchApiNetwork, self).__init__()
        self.device_management_type = request.args.get('type')


class SearchApiWebService(SearchApiApplication):
    def __init__(self):
        super(SearchApiWebService, self).__init__()
        self.device_management_type = request.args.get('type')
        print(self.device_management_type)

# pa_api.add_resource(PaEngine, '/')
# pa_api.add_resource(SearchApiApplication, '/performance-analysis-application/application')
# pa_api.add_resource(SearchApiNetwork, '/performance-analysis-application/network')
