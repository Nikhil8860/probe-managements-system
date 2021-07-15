from db_config import db, ma
from models.networks import network_model
from models.webservices import web_service_model
from models.performance_analysis import performance_model
from sqlalchemy import Column, Integer, ForeignKey


class Domain(db.Model):
    __tablename__ = 'domain'
    domain_id = db.Column(db.Integer, db.Sequence('seq_domain_id', start=101, increment=1), primary_key=True)
    application_id = Column(Integer, ForeignKey(performance_model.Applications.application_id))
    network_id = Column(Integer, ForeignKey(network_model.Network.network_id))
    url_name = Column(Integer, ForeignKey(web_service_model.WebService.url_id))
    domain_name = db.Column(db.String(50))


class DomainSchema(ma.Schema):
    class Meta:
        fields = ('domain_name',)
