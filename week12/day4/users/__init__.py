import flask

from users.config import Config

app = flask.Flask(__name__)
app.config.from_object(Config)

from users import routes
