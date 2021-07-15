from marshmallow import Schema, fields


class BarQuerySchema(Schema):
    id = fields.Integer(required=True)


class SearchSchema(Schema):
    type = fields.String(required=False)
    probe = fields.String(required=False)
    region = fields.String(required=False)
    site_name = fields.String(required=False)
    start_date = fields.String(required=False)
    end_date = fields.String(required=False)


class SearchSchemaDeviceManagement(Schema):
    id = fields.Integer(required=True)
    probe_name = fields.String(required=True)
    region = fields.String(required=True)
    site_name = fields.String(required=True)
    mobile_technology = fields.String(required=True)
    mobile_model = fields.String(required=True)
    cordinates = fields.String(required=True)
    date_of_installation = fields.String(required=True)
    device_id = fields.String(required=True)
    mobile_number = fields.String(required=True)
    mobile_os = fields.String(required=True)
    current_version = fields.String(required=True)
    update = fields.String(required=True)
    remote_management = fields.String(required=True)


class SearchKey(Schema):
    q = fields.String(required=True)


class SearchProbe(Schema):
    probe = fields.String(required=True)


class ValidateRemoteAccess(Schema):
    id = fields.Integer(required=False)
    ip = fields.String(required=True)
    port = fields.Integer(required=False)
    user_name = fields.String(required=True)
    password = fields.String(required=True)


class SearchSchemaDeviceManagement(Schema):
    id = fields.Integer(required=True)
    probe_name = fields.String(required=True)
    region = fields.String(required=True)
    site_name = fields.String(required=True)
    mobile_technology = fields.String(required=True)
    mobile_model = fields.String(required=True)
    cordinates = fields.String(required=True)
    date_of_installation = fields.String(required=True)
    device_id = fields.String(required=True)
    mobile_number = fields.String(required=True)
    mobile_os = fields.String(required=True)
    current_version = fields.String(required=True)
    update = fields.String(required=True)
    remote_management = fields.String(required=False)


class SearchKey(Schema):
    q = fields.String(required=True)


class SearchProbe(Schema):
    probe = fields.String(required=True)


class ValidateRemoteAccess(Schema):
    id = fields.Integer(required=False)
    ip = fields.String(required=True)
    port = fields.Integer(required=False)
    user_name = fields.String(required=True)
    password = fields.String(required=True)
