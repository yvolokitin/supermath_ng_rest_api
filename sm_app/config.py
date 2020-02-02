# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:asdasd12@localhost/supermath_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
