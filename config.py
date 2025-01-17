import os
import redis

from dotenv import load_dotenv

from datetime import datetime

# API VARS IN ENV
env_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(env_dir, '.env'))

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():

    FLASK_ENV= os.environ.get('FLASK_ENV')

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    ROWS_PER_PAGE = 10

    PSQL_PASS = os.environ.get('PSQL_PASS')
    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{PSQL_PASS}@localhost:5432/futbolero"

    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_TYPE = 'redis'
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')
    SESSION_REDIS = redis.Redis(
        host='localhost', 
        port=6379, 
        db=0, 
        password=REDIS_PASSWORD
    )


    ADM_MAIL = os.environ.get('ADM_MAIL')
    ADM_PASS = os.environ.get('ADM_PASS')

