"""
  file: run.py
  author: Andrew Roy Chen
  project: Udacity FSND P3 YAMA
  description:
    Starts local test server using Flask built-in server function.
    Note: instance_config file with app keys are needed to run
"""
from yama import app
from default_course_data import loadDB

# this will setup a local database
loadDB()

app.run(host='0.0.0.0', port=5100)
