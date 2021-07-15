from app import pms_app
from flask_cors import CORS
import config
from db_config import db

CORS(pms_app)
with pms_app.app_context():
    db.create_all()
if __name__ == '__main__':
    pms_app.logger.info('Listening on http://127.0.0.1:5000/')
    pms_app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
