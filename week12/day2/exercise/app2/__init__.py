import flask
from .testkey import Config
from . import routes

app = flask.Flask(__name__)
app.config.from_object(testkey.Config)

