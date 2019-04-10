from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.flaskbasic import application


application.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///db/bellybutton.sqlite"
db = SQLAlchemy(application)

from src.flaskbasic.wsgi import *


