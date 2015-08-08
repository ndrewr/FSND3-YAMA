Udacity Fullstack Nanodegree - Project 3
=====================================================
### YAMA - Yes Another MOOC Aggregrator - a programming course Catalog Application ###
### Author: Andrew Roy Chen, July 2015 ###



SUMMARY:
-----------------------------------------------------
YAMA is an application built with Flask on the backend, SQLAlchemy-ORM assisted database and a front-end utitlizing the Materialize library.

The app integrates User account registration, 3rd party account authentication via Github. Users can select a course category and a list of resources with descriptions and links. A logged-in user can additionally add, edit and delete these course items.  New posts will be tagged with the creator's account name.

The live app demo is on Heroku here:
http://yama-go.herokuapp.com



FILE STRUCTURE:
-----------------------------------------------------
This project packages the application files into the app folder 'yama'. Major modules and folders in the package include:
* views.py - includes app routes
* models.py
* forms.py
* static - static assets
* templates - html files supporting Jinja2

Alongside the app package are the flask configuration files, a module that sets up the default database and the app local development runner 'run.py'.



INSTRUCTIONS TO RUN:
-----------------------------------------------------
This project was first developed using 'Common code for the Relational Databases and Full Stack Fundamentals' courses found here:
http://github.com/udacity/fullstack-nanodegree-vm

The above describes a pre-configured vagrant setup. Quick start detailed here:
http://docs.vagrantup.com/v2/getting-started

Vagrant is **not** required to run the project.

Optional but recommended: setup a virtual environment for running the project. More details:
http://docs.python-guide.org/en/latest/dev/virtualenvs/

Project dependencies are listed under requirements.txt
Pip is used in the example below.
Whichever method, to run locally **ensure the neccessary python modules are already installed**:
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

The Flask webserver is used to test locally but on deployment Gunicorn was used for better concurrent connection handling.

Flask configuration was a minor issue but to allow graders to run the app locally, private key information was included in the repo temporarily.
