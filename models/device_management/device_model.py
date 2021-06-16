from datetime import datetime
from db_config import db, ma


class DeviceManagement(db.Model):
    __tablename__ = "device_management"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    probe_name = db.Column(db.String(32))
    region = db.Column(db.String(32))
    site_name = db.Column(db.String(32))
    mobile_technology = db.Column(db.String(32))
    mobile_model = db.Column(db.String(32))
    cordinates = db.Column(db.String(32))
    date_of_installation = db.Column(db.DateTime, nullable=False, default=datetime.now)
    device_id = db.Column(db.String(32))
    mobile_number = db.Column(db.String(32))
    mobile_os = db.Column(db.String(32))
    current_version = db.Column(db.String(32))
    update = db.Column(db.String(32))
    remote_management = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.utcnow)


class DeviceManagementSchema(ma.Schema):
    class Meta:
        fields = ('id', 'probe_name', 'region', 'site_name', 'mobile_technology', 'mobile_model', 'cordinates',
                  'date_of_installation', 'device_id', 'mobile_number', 'mobile_os',
                  'current_version', 'update', 'remote_management', 'timestamp')
