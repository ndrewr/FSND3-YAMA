# instance config for development
# for deploy on Heroku,
# sensitive keys kept in env vars defined in .env
import os

SECRET_KEY = 'utterly_secret_key'
DEBUG = True # Turns on debugging features in Flask on this dev machine

SQLALCHEMY_DATABASE_URI = 'sqlite:///coursecatalog.db'

#SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
GITHUB_CLIENT_ID = '813ecb2425acd0b32d4d'
GITHUB_CLIENT_SECRET = '6f215bedce49d32df7f5862d6c5c3618d6055e0c'
