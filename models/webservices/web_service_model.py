from db_config import db, ma
from sqlalchemy import Column, Integer, ForeignKey
from models.probe_monitoring import probe_model


class WebService(db.Model):
    __tablename__ = 'urls'
    url_id = db.Column(db.Integer, db.Sequence('seq_urls_id', start=501, increment=1), primary_key=True)
    probe_id = Column(Integer, ForeignKey(probe_model.ProbeMonitoring.probe_id))
    url_name = db.Column(db.String(50))


class WebServiceSchema(ma.Schema):
    class Meta:
        fields = ('url_id', 'probe_id', 'url_name',)
