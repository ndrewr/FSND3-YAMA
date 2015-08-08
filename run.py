from yama import app
from default_course_data import loadDB

# this will setup a local database
loadDB()

app.run(host='0.0.0.0', port=5100)
