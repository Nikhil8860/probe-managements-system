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


class PerformanceAnalysisSchema(ma.Schema):
    class Meta:
        fields = ('id', 'start_date', 'end_date', 'region', 'site_name', 'probe', 'app_type', 'timestamp')
