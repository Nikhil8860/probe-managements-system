from datetime import datetime
from db_config import db, ma


class ProbeMonitoring(db.Model):
    __tablename__ = "probe"
    probe_id = id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    device_id = db.Column(db.String(100))
    probe_display_name = db.Column(db.String(100))
    region = db.Column(db.String(100))
    site_name = db.Column(db.String(100))
    mobile_technology = db.Column(db.String(100))
    mobile_model = db.Column(db.String(100))
    mobile_number = db.Column(db.String(100))
    mobile_os = db.Column(db.String(100))
    mobile_os_version = db.Column(db.String(100))
    current_version = db.Column(db.String(100))
    current_status = db.Column(db.String(100))
    cordinates = db.Column(db.String(200))
    default_select = db.Column(db.Integer)
    installation_date = db.Column(db.DateTime, nullable=False)
    installation_by = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.utcnow)


class ProbeMonitoringSchema(ma.Schema):
    class Meta:
        fields = ('probe_id', 'device_id', 'probe_display_name', 'region', 'site_name', 'mobile_technology',
                  'mobile_model', 'mobile_number', 'mobile_os', 'mobile_os_version', 'current_version',
                  'current_status',
                  'cordinates', 'default_select', 'installation_date', 'installation_by', 'timestamp')
