import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    firstname = wtforms.StringField("First name", wtforms.validators.Required)
    lastname = wtforms.StringField("Last name", wtforms.validators.Required)
    age = wtforms.IntegerField("Age", wtforms.validators.Length)
    experience = wtforms.StringField("Experience")
    city = wtforms.StringField("In which city do you live?")

