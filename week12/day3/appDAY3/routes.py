import flask
from flask import flash
from flask import Flask, render_template

app = flask.Flask(__name__)


@app.route("/")
def flash_ex():
    flash("Hey", "blue")
    flash("HEY", "red")
    return render_template("index.html")




