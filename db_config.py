from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import pms_app

# sqlite_url = "postgresql://postgres:nikhil@localhost:5432/probe_management_system"
sqlite_url = "postgresql://postgres:nikhil@localhost:5432/probe_management_system"
pms_app.config["SQLALCHEMY_ECHO"] = True
pms_app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
pms_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SqlAlchemy db instance
db = SQLAlchemy(pms_app)

# Initialize Marshmallow
ma = Marshmallow(pms_app)