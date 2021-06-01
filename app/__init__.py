import logging

from .device_management import application
from .performance_analysis import pa
from .fault_management import fm
from .probe_monitoring import pm
from flask import Flask
from config import pms_app
# from run_pms import pms_app

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

with pms_app.app_context():
    pms_app.register_blueprint(pa)
    logging.info("Performance Analysis started")

    pms_app.register_blueprint(application)
    logging.info("Device Management started")

    pms_app.register_blueprint(fm)
    logging.info("Fault Management started")

    pms_app.register_blueprint(pm)
    logging.info("Probe Monitoring started")
