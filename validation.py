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
