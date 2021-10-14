import flask

from app2 import testkey


app = flask.Flask(__name__)
app.config.from_object(testkey.Config)

list_of_cities = []

import app2.routes
import app2.form