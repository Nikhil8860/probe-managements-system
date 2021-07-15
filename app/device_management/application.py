import os
import platform
import datetime
from flask_restful import Resource, Api
from flask import request, make_response, jsonify, abort, current_app, redirect
from . import application
from app import logging
from models.device_management import device_model
from validation import (BarQuerySchema, SearchSchema, SearchSchemaDeviceManagement, SearchKey, ValidateRemoteAccess)
from db_config import db
import json
from sqlalchemy import or_, func
from check_update import remote_access, version_update

application_api = Api(application)

schema = BarQuerySchema()
schema_search = SearchSchema()
SearchSchemaDeviceManagement = SearchSchemaDeviceManagement()
search_key_schema = SearchKey()
validate_remote_access_schema = ValidateRemoteAccess()


class OpenTerminal(Resource):
    def get(self):
        os.system("start cmd")
        # os.popen("Start cmd cd ../")
        # command = ["python", "mytool.py", "-a", servers[server]['address'],
        #            "-x", servers[server]['port'],
        #            "-p", servers[server]['pass'],
        #            "some", "additional", "command"]
        command = ["dir"]
        # p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        # p1 = subprocess.Popen('dir', shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # p2 = subprocess.Popen('sort /R', shell=True, stdin=p1.stdout)
        #
        # p1.stdout.close()
        # out, err = p2.communicate()
        # print(out)
        # print(err)
        return redirect('http://localhost:4200/')


# @application_api.resource('/')
class DeviceManagementEngine(Resource):
    def get(self):
        time_24_hr_ago = (datetime.datetime.now() - datetime.timedelta(days=1)).date().strftime('%Y-%m-%d')
        #  here we will get last 24 hr data by default
        id = request.args.get('id')
        if id:
            # device_data = device_model.DeviceManagement.query.filter_by(id=id, timestamp=datetime.datetime.now().date().strftime('%Y-%m-%d'))
            device_data = device_model.DeviceManagement.query.filter_by(id=id)
        else:
            device_data = device_model.DeviceManagement.query.all()
            # device_data = device_model.DeviceManagement.query.filter(
            #     func.Date(device_model.DeviceManagement.timestamp) == time_24_hr_ago)
        # Serialize the data for the response
        device_management_schema = device_model.DeviceManagementSchema(many=True)
        result = device_management_schema.dump(device_data)
        print(result)
        current_app.logger.info("Result")
        current_app.logger.info(result)
        if result:
            return make_response({"status": True, "data": result})
        else:
            return make_response({"status": False, "data": []})

    def post(self):
        return make_response(jsonify({"msg": "POSt"}))

    def put(self):
        # open command promp only and leave it
        errors = SearchSchemaDeviceManagement.validate(request.json)
        if errors:
            abort(400, str(errors))
        id = request.json['id']
        logging.info("Id")
        logging.info(id)
        rec = device_model.DeviceManagement.query.filter_by(id=id).first()
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
            rec = device_model.DeviceManagement.query.filter_by(id=id)
            device_management_schema = device_model.DeviceManagementSchema(many=True)
            result = device_management_schema.dump(rec)
            with open('./resources/probe.json', 'w') as f:
                f.write(json.dumps(result, indent=4))
            return make_response({"msg": "Record has been updated"}, 202)
        else:
            return make_response({"msg": "Record does not exist"}, 404)


class DeviceManagementUpdate(Resource):
    def get(self):
        return {"msg": "Success"}

    def put(self):
        id = request.json['id']
        # id = 1
        logging.info("Id")
        logging.info(id)
        errors = validate_remote_access_schema.validate(request.json)
        if errors:
            abort(400, str(errors))
        ip = request.json['ip']
        if request.json['port']:
            port = request.json['port']
        else:
            port = 6022
        user_name = request.json['user_name']
        password = request.json['password']
        # print(ip, port, user_name, password)
        cmd, version = version_update.get_user_name_password(ip, port, user_name, password)
        rec = device_model.DeviceManagement.query.filter_by(id=id).first()
        current_version = float(rec.current_version)
        present_version = float(rec.update.split()[-1])

        if current_version < version:
            os.system(cmd)
            print("Hello")
            return make_response({"status": True, "msg": cmd}, 202)

        #     print("Run the ssh command and check for new update")
        #     if rec:
        #         rec.update = request.json['update']
        #         db.session.commit()
        #         return make_response({"msg": "Record has been updated"}, 202)
        #     else:
        #         return make_response({"msg": "Record does not exist"}, 404)
        # else:
        #     pass


class DeviceManagementRemoteAccessApi(Resource):
    def get(self):
        print(request.url)
        if platform.system() == 'Windows':
            os.system('start cmd /k "color a & cd ../ & dir"')
        # errors = schema.validate(request.args)
        # print(errors)
        # if errors:
        #     abort(400, str(errors))
        #
        # id = request.args.get('id')
        # rec = device_model.DeviceManagement.query.filter_by(id=id)
        # device_management_schema = device_model.DeviceManagementSchema(many=True)
        # result = device_management_schema.dump(rec)
        # return redirect('http://localhost:4200/')
        return make_response({"status": True})
        # if result:
        #     return make_response({"status": True, "data": result})
        # else:
        #     return make_response({"status": False, "data": []})

    def post(self):
        # This will open command CLI after ssh login
        errors = validate_remote_access_schema.validate(request.form)
        if errors:
            abort(400, str(errors))
        ip = request.form['ip']
        if request.form['port']:
            port = request.form['port']
        else:
            port = 6022
        user_name = request.form['user_name']
        password = request.form['password']
        print(ip, port, user_name, password)
        cmd = remote_access.get_user_name_password(ip, port, user_name, password)
        os.system(cmd)
        return make_response({"status": True, "cmd": cmd})


class SearchApi(Resource):

    def get(self):
        errors = search_key_schema.validate(request.args)
        if errors:
            abort(400, str(errors))
        search_key = request.args.get('q')
        results = device_model.DeviceManagement.query.filter(or_(device_model.DeviceManagement.update == search_key,
                                                                 device_model.DeviceManagement.region == search_key,
                                                                 device_model.DeviceManagement.device_id == search_key,
                                                                 device_model.DeviceManagement.remote_management == search_key,
                                                                 device_model.DeviceManagement.current_version == search_key,
                                                                 device_model.DeviceManagement.site_name == search_key,
                                                                 device_model.DeviceManagement.probe_name == search_key,
                                                                 device_model.DeviceManagement.mobile_os == search_key,
                                                                 device_model.DeviceManagement.mobile_model == search_key,
                                                                 device_model.DeviceManagement.mobile_number == search_key,
                                                                 device_model.DeviceManagement.mobile_technology == search_key,
                                                                 device_model.DeviceManagement.cordinates == search_key))
        device_management_schema = device_model.DeviceManagementSchema(many=True)
        result = device_management_schema.dump(results)

        if result:
            return {"status": True, "msg": result}
        else:
            return {"status": False, "msg": "No Data Found"}
