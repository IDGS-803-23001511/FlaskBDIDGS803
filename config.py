from re import DEBUG
from sqlalchemy import create_engine

class Config(object)
    SECRET_KEY=0"ClaveSecreta"
    SESSION_COOKIE_SECURE=False

class DevelopmentConfig (Config)
    DEBUG=True
    SQALCHEMY_DATABASE_URI='mysql+pymsql://root:isabb150108@127.0.0.1/bdidgs803'
    SQALCHEMY_TRACK_MODIFICATIONS=False    