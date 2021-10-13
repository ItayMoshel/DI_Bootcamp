import flask
from flask import Flask, render_template

from app3 import app
from app3 import forms


@app.route("/home")
def home():
    return render_template("base.html")


@app.route("/", methods=("GET", "POST"))
def form():
    form = forms.Form()
    if form.validate_on_submit():  # Check if the form has been filled
        firstname = form.firstname.data
        lastname = form.lastname.data
        age = form.age.data
        experience = form.experience.data
        city = form.city.data

        print("Here is what I got from the form:")
        print("First name: ", firstname)
        print("Last name: ", lastname)
        print("Age: ", age)
        print("Experience: ", experience)
        print("City: ", city)

        return flask.redirect('/home')
    return render_template("baseform.html", form=form)
