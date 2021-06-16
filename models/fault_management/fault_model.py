from datetime import datetime
from db_config import db, ma


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
    comment = db.Column(db.String(255))
    ack_time = db.Column(db.DateTime, nullable=False, default=datetime.now)


class FaultManagementSchema(ma.Schema):
    class Meta:
        fields = ('fault_id', 'time', 'probe_id', 'region', 'site_name', 'ip', 'fault_description', 'current_version',
                  'status', 'ack_by', 'ack_time', 'comment')
