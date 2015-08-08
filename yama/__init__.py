from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.github import GitHub
import os


#app = Flask(__name__)
app = Flask(__name__, instance_relative_config=True)

if os.environ.get('HEROKU_DEPLOY') is None:
  app.config.from_pyfile('instance_config.py')
else:
  app.config.from_object('default_config')

db = SQLAlchemy(app)

# for user authentication via github
github = GitHub(app)


# this definition must follow app instantiation to hookup access to views
from yama import views, models
