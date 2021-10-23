from Week13.day4.phone.app import app, db

from flask import redirect, render_template

from Week13.day4.phone.app.models import Phonenumber, Person


@app.route('/')
def index():
	return 'Hello'

@app.route('/person/<phonenumber>')
def display_info_acoording_to_phonenumber(phonenumber):
		phonenumber_info = Phonenumber.query.filter_by(number=phonenumber).first()
		person_id = phonenumber_info.person_id

		person_info = Person.query.filter_by(id=person_id).first()

		return f'Name:{person_info.name}<br>Email: {person_info.email}<br>Phone number: {phonenumber}'


# to get the values of a relationship attribute you can run the following:
#  person_info.phonenumbers.all()[1].number
