from users import app
import flask
from flask import render_template


@app.route("/")
def base():
    return render_template("base.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/main")
def main():
    return render_template("main.html")


@app.route("/form")
def form():
    return render_template("form.html")