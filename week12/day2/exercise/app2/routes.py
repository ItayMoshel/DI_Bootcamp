from flask import render_template
import flask
from app2 import app, list_of_cities
from app2.form import Form


@app.route('/add-city', methods=("GET", "POST"))
def add_city():
    form = Form()
    if form.validate_on_submit():
        cityname = form.cityname.data
        citycountry = form.citycountry.data
        numofinhabitants = form.numofinhabitats.data
        cityarea = form.cityarea.data
        capital = form.is_capital
        dict = {
            "city name": cityname,
            "city country": citycountry,
            "city area": cityarea,
            "number of inhabitants": numofinhabitants,
            "capital": capital,
        }
        list_of_cities.append(dict)

        return flask.redirect('/')
    return render_template("add_city.html", form=form)


@app.route("/")
def home():
    return f"{list_of_cities}"


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template("404.html"), 404


