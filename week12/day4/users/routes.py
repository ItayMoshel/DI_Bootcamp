from users import app
import flask
from flask import render_template

# from users.form import Form


@app.route("/base")
def base():
    return render_template("base.html")


@app.route("/")
def home():
    return render_template("home.html")


# @app.route("form", methods=("GET", "POST"))
# def form():
#     form = Form()
#     return render_template("form.html", form=form)


@app.route("/main")
def main():
    render_template("main.html")
