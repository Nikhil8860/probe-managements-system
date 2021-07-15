from datetime import datetime
from db_config import db, ma


class PerformanceAnalysis(db.Model):
    __tablename__ = "performance_analysis"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    end_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    region = db.Column(db.String(32))
    site_name = db.Column(db.String(32))
    probe = db.Column(db.String(32))
    app_type = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.utcnow
    )


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


class FaultManagement(db.Model):
    __tablename__ = "fault_management"
    fault_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    probe_id = db.Column(db.String(32))
    region = db.Column(db.String(32))
    site_name = db.Column(db.String(32))
    ip = db.Column(db.String(32))
    fault_description = db.Column(db.String(100))
    current_version = db.Column(db.String(32))
    status = db.Column(db.String(32))
    ack_by = db.Column(db.String(32))
    ack_time = db.Column(db.DateTime, nullable=False, default=datetime.now)


class PerformanceAnalysisSchema(ma.Schema):
    class Meta:
        fields = ('id', 'start_date', 'end_date', 'region', 'site_name', 'probe', 'app_type', 'timestamp')


class DeviceManagementSchema(ma.Schema):
    class Meta:
        fields = ('id', 'probe_name', 'region', 'site_name', 'mobile_technology', 'mobile_model', 'cordinates',
                  'date_of_installation', 'device_id', 'mobile_number', 'mobile_os',
                  'current_version', 'update', 'remote_management', 'timestamp')


class FaultManagementSchema(ma.Schema):
    class Meta:
        fields = ('fault_id', 'time', 'probe_id', 'region', 'site_name', 'ip', 'fault_description', 'current_version',
                  'status', 'ack_by', 'ack_time')


class FaultManagementSchema(ma.Schema):
    class Meta:
        fields = ('fault_id', 'time', 'probe_id', 'region', 'site_name', 'ip', 'fault_description', 'current_version',
                  'status', 'ack_by', 'ack_time')
