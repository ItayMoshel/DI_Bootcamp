import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    cityname = wtforms.StringField("City's Name")
    citycountry = wtforms.StringField("City's country")
    numofinhabitats = wtforms.IntegerField("Number of inhabitants")
    cityarea = wtforms.IntegerField("City's area in KM")
