from flask import Flask
from app.config import config_options
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config_options["dev_config"])
api = Api(app)
db = SQLAlchemy(app)

from app import views