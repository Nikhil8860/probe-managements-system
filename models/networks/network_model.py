from db_config import db, ma
from models.probe_monitoring import probe_model
from sqlalchemy import Column, Integer, ForeignKey


class Network(db.Model):
    __tablename__ = 'network'
    network_id = db.Column(db.Integer, primary_key=True)
    probe_id = Column(Integer, ForeignKey(probe_model.ProbeMonitoring.probe_id))
    network_name = db.Column(db.String(50))
    dpi = db.Column(db.String(50))
    network_display_name = db.Column(db.String(50))


class NetworkSchema(ma.Schema):
    class Meta:
        fields = ('network_id', 'probe_id', 'network_name', 'dpi', 'network_display_name')
