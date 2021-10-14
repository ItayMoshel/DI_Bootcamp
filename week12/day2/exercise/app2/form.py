import flask_wtf
import wtforms


def positive_num(num):
    if num % 2 == 0:
        return num


class Form(flask_wtf.FlaskForm):
    cityname = wtforms.StringField("City's Name", [wtforms.validators.DataRequired()])
    citycountry = wtforms.StringField("City's country", [wtforms.validators.DataRequired()])
    numofinhabitats = wtforms.IntegerField("Number of inhabitants", [wtforms.validators.DataRequired()])
    cityarea = wtforms.IntegerField("City's area in KM")
    latitude = wtforms.IntegerField("latitude")
    longitude = wtforms.IntegerField("longitude")
    is_capital = wtforms.BooleanField("capital")
    submit = wtforms.SubmitField("Submit")

