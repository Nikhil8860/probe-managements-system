from flask_restful import Resource
from flask import request, make_response, abort, jsonify
from db_config import db
from validation import BarQuerySchema, SearchSchema, SearchProbe
from models.performance_analysis import performance_model
from models.networks import network_model
from models.webservices import web_service_model
from app import logging
import datetime
from sqlalchemy import func
from lookup_data.mapper import urls
import requests

schema = BarQuerySchema()
schema_search = SearchSchema()
search_probe = SearchProbe()


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
        self.result = None

    def get(self):
        dynamic_query = ""
        errors = schema_search.validate(request.args)
        if errors:
            abort(400, str(errors))
        if not self.probe and not self.site_name and not self.start_date and not self.end_date:
            url = urls[self.device_management_type.lower()]
            self.result = requests.get(url).json()
        if self.probe and self.region and self.site_name and self.start_date and self.end_date and self.device_management_type:
            self.start_date = datetime.datetime.strptime(self.start_date, '%Y-%m-%d')
            self.end_date = datetime.datetime.strptime(self.end_date, '%Y-%m-%d')
            diff = self.end_date - self.start_date
            days, seconds = diff.days, diff.seconds
            hours = days * 24 + seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            print(hours)
            self.query_dict = {"probe": self.probe, "region": self.region, "site_name": self.site_name,
                               "start_date": self.start_date,
                               "end_date": self.end_date, "app_type": self.device_management_type}
            url = urls[self.device_management_type.lower()].replace("time > now() - 24h", "time > now() - {}h").format(
                hours)

            dynamic_query += f" AND SiteName='{self.site_name}' AND Region='{self.region}'"
            print(url + dynamic_query)
            self.result = requests.get(url + dynamic_query).json()

        # print(self.query_dict)
        # if len(self.query_dict) == 0:
        #     time_24_hr_ago = (datetime.datetime.now() - datetime.timedelta(days=1)).date().strftime('%Y-%m-%d')
        #     results = performance_model.PerformanceAnalysis.query.filter(
        #         func.Date(performance_model.PerformanceAnalysis.timestamp) == time_24_hr_ago)
        #     # results = performance_model.PerformanceAnalysis.query.all()
        # else:
        #     results = performance_model.PerformanceAnalysis.query.filter_by(**self.query_dict).all()
        #
        # performance_analysis = performance_model.PerformanceAnalysisSchema(many=True)
        # self.result = performance_analysis.dump(results)

        if self.result:
            return self.result
        else:
            return {"status": False, "data": []}

    def post(self):
        probe = request.json['probe']
        logging.info("Probe from request" + str(probe))
        test = performance_model.PerformanceAnalysis.query.filter_by(probe=probe).first()
        if test:
            return make_response(jsonify({'msg': "Result already exists"}, 409))
        else:
            start_date = datetime.datetime.strptime(request.json['start_date'], '%d/%m/%Y')
            end_date = datetime.datetime.strptime(request.json['end_date'], '%d/%m/%Y')
            region = request.json['region']
            site_name = request.json['site_name']
            probe = request.json['probe']
            app_type = request.json['app_type']
            p = performance_model.PerformanceAnalysis(start_date=start_date, end_date=end_date, region=region,
                                                      site_name=site_name,
                                                      probe=probe, app_type=app_type)
            db.session.add(p)
            db.session.commit()
            return make_response({"msg": "Data has been Inserted"}, 201)

    def delete(self):
        id = request.args.get('id')
        rec = performance_model.PerformanceAnalysis.query.filter_by(id=id).first()
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


class SearchApiProbe(Resource):
    def get(self):
        errors = search_probe.validate(request.args)
        if errors:
            abort(400, str(errors))
        probe_name = request.args.get('probe', None)
        if probe_name:
            data = requests.get(urls[probe_name.lower()])
        #     print(data.json())
        # print(probe_name)
        # results = performance_model.PerformanceAnalysis.query.filter_by(probe=probe_name).all()
        # performance_analysis = performance_model.PerformanceAnalysisSchema(many=True)
        # result = performance_analysis.dump(results)
        # if result:
        #     return make_response({"status": True, "data": result})
        # else:
        #     return make_response({"status": False, "data": "No Data Found"})
        return make_response(data.json())


class GetProbe(Resource):
    def get(self):
        data = performance_model.Applications.query.all()
        performance_analysis = performance_model.ApplicationSchema(many=True)
        result = performance_analysis.dump(data)
        result = [i['application_name'] for i in result]
        if result:
            return {"status": True, "data": result}
        else:
            return {"status": False, "data": []}


class GetNetwork(Resource):
    def get(self):
        print("HELLO")
        data = network_model.Network.query.all()
        network_analysis = network_model.NetworkSchema(many=True)
        result = network_analysis.dump(data)
        result = list(set([i['network_name'] for i in result]))
        if result:
            return {"status": True, "data": result}
        else:
            return {"status": False, "data": []}


class GetWebServices(Resource):
    def get(self):
        data = web_service_model.WebService.query.all()
        web_service_data = web_service_model.WebServiceSchema(many=True)
        result = web_service_data.dump(data)
        result = list(set([i['url_name'] for i in result]))
        if result:
            return {"status": True, "data": result}
        else:
            return {"status": False, "data": []}

# pa_api.add_resource(PaEngine, '/')
# pa_api.add_resource(SearchApiApplication, '/performance-analysis-application/application')
# pa_api.add_resource(SearchApiNetwork, '/performance-analysis-application/network')
