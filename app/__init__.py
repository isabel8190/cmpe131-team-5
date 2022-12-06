from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#from config import Config
#from flask_migrate import Migrate

myapp_obj = Flask(__name__)
#myapp_obj.config.from_object(Config)

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.update(                    #app.config.from_mapping(
    SECRET_KEY='this-is-a-secret',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),   #sets location of database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)
db = SQLAlchemy(myapp_obj)
#migrate = Migrate(myapp_obj,db)

login = LoginManager(myapp_obj)

login.login_view = 'login'

from app import routes, models



 