Udacity Fullstack Nanodegree - Project 3
=====================================================
### YAMA - Yes Another MOOC Aggregrator - a programming course Catalog Application ###
### Author: Andrew Roy Chen, July 2015 ###


SUMMARY:
-----------------------------------------------------
YAMA is an application built with Flask on the backend, SQLAlchemy database api and a front-end Materialize framework.
The app integrates User account registration, 3rd party account authentication via Github.
Users can select a course category and a list of resources with descriptions and links. A logged-in user can additionally add, edit and delete these course items.


FILE STRUCTURE:
-----------------------------------------------------
This project is expanded from the 'Common code for the Relational Databases and Full Stack Fundamentals' courses found here:
http://github.com/udacity/fullstack-nanodegree-vm

The project uses a pre-configured vagrant setup. Quick start detailed here:
http://docs.vagrantup.com/v2/getting-started

Actual project code is located in the directory:
```
./vagrant/catalog
```


INSTRUCTIONS TO RUN:
-----------------------------------------------------
Vagrant is not required to run the project. Project dependencies are listed under requirements.txt
Pip is used in the example below.

Optional but recommended: setup a virtual environment for running the project. More details:
http://docs.python-guide.org/en/latest/dev/virtualenvs/

Ensure the following python modules are already installed:
```
pip install -r requirements.txt
```

Next to run on localhost:5100 (yes, 5100) simply:
```
python run.py
```

The above file will initialize a sample course database and start the app running locally on port 5100.
The test server uses Flask's built-in web server.

Users can view any course details but must login with Github credentials to access Create, Update and Delete privileges.


DEVELOPMENT NOTES:
-----------------------------------------------------
The project uses the Flask microframework and several key extensions to aid development. Data is stored in local test environment using SQLite but on deployment to Heroku PostgreSQL was used.

The Flask webserver is used to test locally but on deployment Gunicorn was used.
