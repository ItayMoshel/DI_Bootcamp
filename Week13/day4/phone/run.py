import random
from faker import Faker
from Week13.day4.phone.app import app, db
from Week13.day4.phone.app.models import Person, Phonenumber


def addFakePersons():
    print('add fake persons')
    fake = Faker()

    for _ in range(20):
        name = fake.first_name()
        email = fake.email()
        address = fake.address()
        person = Person(name=name, email=email, address=address)
        db.session.add(person)

    db.session.commit()


def addFakePhoneNumbers():
    print('add fake phones')
    fake = Faker()

    persons = Person.query.all()

    for _ in range(20):
        phone_number = fake.phone_number()
        rand_person_num = random.randint(0, len(persons) - 1)
        phone_number = Phonenumber(number=phone_number, person_id=persons[rand_person_num].id)
        db.session.add(phone_number)

    db.session.commit()


if __name__ == '__main__':
    addFakePersons()
    addFakePhoneNumbers()
    app.run(debug=True)
