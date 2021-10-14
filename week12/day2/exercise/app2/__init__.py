import flask

from app2 import testkey


app = flask.Flask(__name__)
app.config.from_object(testkey.Config)

import app2.routes
import app2.form