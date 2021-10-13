import flask
from . import app


@app.errorhandler(404)
def error_404(error):
    return flask.render_template("errors/404er.html"), 404


@app.errorhandler(500)
def error_500(error):
    return flask.render_template("errors/500er.html"), 500
