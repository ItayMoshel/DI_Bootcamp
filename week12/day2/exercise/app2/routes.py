from flask import Flask, render_template, render_template_string
from .form import Form
import flask

app = Flask(__name__)

form_template = """
    <form method="POST">
    {{ form.hidden_tag() }}

    {{ form.firstname.label }}
    {{ form.firstname(size=20) }}

    {{ form.lastname.label }}
    {{ form.lastname(size=20) }}

    {{ form.age.label }}
    {{ form.age(size=3) }}

    {{ form.username.label }}
    {{ form.username(size=32) }}

    {{ form.password.label }}
    {{ form.password(size=32) }}

    {{ form.bio.label }}
    {{ form.bio(size=240) }}

    {{ form.submit() }}
    </form>
    """


@app.route("/")
def home():
    return render_template("base.html")


@app.route('/myform', methods=("GET", "POST"))
def myform():
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
    return render_template_string(form_template, form=form)
