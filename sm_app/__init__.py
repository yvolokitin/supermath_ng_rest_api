import logging

from flask import Flask
# from flask import Flask, request, jsonify
from flask_mail import Mail
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy

from sm_app.config import Config

sm_app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

mail_settings = {
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 465,
    'MAIL_USE_TLS': False,
    'MAIL_USE_SSL': True,
    'MAIL_USERNAME': 'supermath.xyz@gmail.com',
    'MAIL_PASSWORD': 'fivdrrlgzntzqtiz'
}

sm_app.config.update(mail_settings)
mail = Mail(sm_app)
CORS(sm_app)
sm_app.config.from_object(Config)
sm_db = SQLAlchemy(sm_app)

from sm_app import routes, user, result, userinfo, emailer
