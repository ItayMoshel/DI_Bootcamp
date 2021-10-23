from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import os
import sys

sys.path.append("/Users/itaym/DI_Bootcamp")

# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True
os.system('export FLASK_APP=/Users/itaym/DI_Bootcamp/Week13/day4/phone/run.py')


# Database Connection
db_info = {'host': 'localhost',
		   'database': 'phone_store',
		   'psw': '1234',
		   'user': 'postgres',
		   'port': ''}
app.config[
	'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from Week13.day4.phone.app import models, routes
