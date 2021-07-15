from datetime import datetime
from db_config import db, ma
from models.probe_monitoring import probe_model
from sqlalchemy import Column, Integer, ForeignKey


class FaultManagement(db.Model):
    __tablename__ = "faults"
    fault_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    probe_id = Column(Integer, ForeignKey(probe_model.ProbeMonitoring.probe_id))
    time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    region = db.Column(db.String(32))
    site_name = db.Column(db.String(32))
    ip = db.Column(db.String(32))
    fault_description = db.Column(db.String(100))
    current_version = db.Column(db.String(32))
    status = db.Column(db.String(32))
    ack_by = db.Column(db.String(32))
    comment = db.Column(db.String(255))
    ack_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    timestamp = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.utcnow)


class FaultManagementSchema(ma.Schema):
    class Meta:
        fields = (
        'fault_id', 'probe_id', 'time', 'probe_id', 'region', 'site_name', 'ip', 'fault_description', 'current_version',
        'status', 'ack_by', 'ack_time', 'comment', 'timestamp')
