import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLACHEMY_DATABASE_URI = 'sqlite:///./app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # adding secret key for the CSRF tocken 
    SECRET_KEY = 'Im a secret key'
