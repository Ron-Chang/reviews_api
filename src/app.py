import redis
from config import Config
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

config = Config()
app.config.from_object(config)

spider_rs = redis.StrictRedis(
    host=config.SPIDER_REDIS_HOST,
    password=config.SPIDER_REDIS_PASSWORD,
    port=config.REDIS_PORT,
    charset='utf-8',
    decode_responses=True)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
db = SQLAlchemy(app)

from controllers.route_controllers import *

from common.models import *



def create_app():
    return app
