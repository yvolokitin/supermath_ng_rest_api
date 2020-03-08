from flask import Flask, request, jsonify
from flask_cors import CORS

from sm_app.config import Config

from flask_sqlalchemy import SQLAlchemy

sm_app = Flask(__name__)
CORS(sm_app)
sm_app.config.from_object(Config)
sm_db = SQLAlchemy(sm_app)

from sm_app import routes, user, result
