import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    firstname = wtforms.StringField("First Name")
    lastname = wtforms.StringField("Last Name")
    age = wtforms.IntegerField()
    username = wtforms.StringField("Username")
    password = wtforms.PasswordField("Password")
    bio = wtforms.StringField("Bio")
    submit = wtforms.SubmitField("Submit")
