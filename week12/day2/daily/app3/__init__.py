import flask
from .config import Config


app = flask.Flask(__name__)
app.config.from_object(config.Config)

from app3 import routes, forms
