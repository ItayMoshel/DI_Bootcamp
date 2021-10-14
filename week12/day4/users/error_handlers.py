from users import app
import flask


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return flask.render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(error):
    print(error)
    return flask.render_template("500.html"), 500
