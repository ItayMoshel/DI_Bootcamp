# First, we are in a different file, so we need to import the app
import flask
from . import app  # app.app is package_name.variable_name
from day1.app.forms import Form


@app.route("/in")
def index():
    posts = [
        {"author": "John", "body": "I love python"},
        {"author": "Fish", "body": "I love water"},
        {"author": "Herpetolog", "body": "I love pythons"},
    ]
    return flask.render_template('index.html', posts=posts)


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


@app.route('/myform', methods=("GET", "POST"))
def myform():
    form = Form()
    if form.validate_on_submit():  # Check if the form has been filled
        firstname = form.firstname.data
        lastname = form.lastname.data
        age = form.age.data
        username = form.username.data  # Get
        password = form.password.data  # The
        bio = form.bio.data  # Data

        print("Here is what I got from the form:")
        print("First name: ", firstname)
        print("Last name: ", lastname)
        print("Age: ", age)
        print("username: ", username)
        print("password: ", password)
        print("bio: ", bio)
        # Do something with the data

        return flask.redirect('/')
    return flask.render_template_string(form_template, form=form)
