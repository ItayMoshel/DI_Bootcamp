import forms
import flask
from flask import Flask, render_template
from app3 import app


@app.route("/")
def home():
    form = forms.Form()
    return render_template("base.html", form=form)

