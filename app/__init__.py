import logging

from .device_management import application
from .performance_analysis import pa
from .fault_management import fm
from .probe_monitoring import pm
from flask import Flask
from config import pms_app
# from run_pms import pms_app

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

with pms_app.app_context():
    pms_app.register_blueprint(pa)
    logging.info("Performance Analysis started")

    pms_app.register_blueprint(application)
    logging.info("Device Management started")

    pms_app.register_blueprint(fm)
    logging.info("Fault Management started")

    pms_app.register_blueprint(pm)
    logging.info("Probe Monitoring started")
