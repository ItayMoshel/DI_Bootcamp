from W9D2E2 import Family

class TheIncredibles(Family):
    members = [
        {'name': 'Bob', 'age': 48, 'gender': 'Male', 'is_child': False, 'power': 'superhuman strength',
         'incredible_name': 'Mr. Incredible'},
        {'name': 'Helen', 'age': 45, 'gender': 'Female', 'is_child': False, 'power': 'elastic women',
         'incredible_name': 'Elastigirl'},
        {'name': 'Violet', 'age': 15, 'gender': 'Female', 'is_child': True, 'power': 'invisibility,Force Fields',
         'incredible_name': 'V'},
        {'name': 'Dashiell', 'age': 10, 'gender': 'Male', 'is_child': True, 'power': 'super speed',
         'incredible_name': 'Dash'},
        # {'name': 'John Jackson', 'age': 1, 'gender': 'Male', 'is_child': True, 'power': 'telekinesis',
        #  'incredible_name': None}
    ]

    def power(self, name):
        for member in TheIncredibles.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(member['name'], member['power'])
                else:
                    raise Exception(f"{name} is not 18 years old.")

    def incredible_presentation(self):
        for member in TheIncredibles.members:
            print(f"Incredible name: {member['incredible_name']}\nPower: {member['power']}")

    def born(self, **kwargs):
        TheIncredibles.members.append(kwargs)


family2 = TheIncredibles("Parr")
family2.incredible_presentation()
family2.power('Bob')
family2.born(name='John Jackson', age=1, gender='Male', is_child=True, power='Unknown', incredible_name=None)
family2.incredible_presentation()
