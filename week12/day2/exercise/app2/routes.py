from flask import Flask, render_template

import flask

from app2 import app
from app2.form import Form


@app.route("/")
def home():
    return render_template("base.html")


@app.route('/add-city', methods=("GET", "POST"))
def add_city():
    form = Form()
    if form.validate_on_submit():  # Check if the form has been filled
        cityname = form.cityname.data
        citycountry = form.citycountry.data
        numofinhabitants = form.numofinhabitats.data
        cityarea = form.cityarea.data

        print("Here is what I got from the form:")
        print("City's name: ", cityname)
        print("City's country: ", citycountry)
        print("City's area : ", cityarea)
        print("Number of inhabitants : ", numofinhabitants)

        return flask.redirect('/')
    return render_template("add_city.html", form=form)


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template("404.html"), 404
