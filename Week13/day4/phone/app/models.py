from Week13.day4.phone.app import db


class Person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	email = db.Column(db.String(64))
	address = db.Column(db.String(255))
	nationality = db.relationship('Nationality', backref='people', lazy='dynamic ')
	nationality_id = db.Column(db.Integer, db.ForeignKey('nationality.id'))
	phonenumbers = db.relationship('Phonenumber', backref='person', lazy='dynamic')

	def __repr__(self):
		return f'<Person: {self.id}, {self.name}, {self.email}, {self.address}, {self.phonenumbers}>'


class Phonenumber(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	number = db.Column(db.String(64))

	person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

	def __repr__(self):
		return f'<Phonenumber: {self.id}, {self.number}, {self.person_id}>'


class Nationality(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	number = db.Column(db.String(64))
	people = db.relationship('Person', backref='nationality', lazy='dynamic ')
	person_id = db.Column(db.Integer, db.ForeignKey('person.id'))



