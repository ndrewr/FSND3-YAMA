# common config options
# sensitive keys stored via heroku env vars
import os

DEBUG = False
CSRF_ENABLED = True
SECRET_KEY = os.environ['SECRET_KEY']

if os.environ.get('DATABASE_URL') is None:
  SQLALCHEMY_DATABASE_URI = 'sqlite:///coursecatalog.db'
else:
  SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

GITHUB_CLIENT_ID = os.environ['GITHUB_CLIENT_ID']
GITHUB_CLIENT_SECRET = os.environ['GITHUB_CLIENT_SECRET']
