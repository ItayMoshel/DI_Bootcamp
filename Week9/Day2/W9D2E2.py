class Family:
    members = [
        {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
    ]
    last_name = ""

    def __init__(self, family_name):
        self.family_name = family_name
        Family.last_name = family_name

    def born(self, **kwargs):
        Family.members.append(kwargs)
        print("Congratulations!")

    def is_18(self, name):
        for member in Family.members:
            if name in member.values():
                return True if member.get('age') >= 18 else False

    def member_printer(self):
        for member in Family.members:
            print(member['name'])



# family1 = Family("Adams")
# print(family1.members)
# family1.born(name="Itay", age=0, gemder="Male", is_child=True)
# print(family1.members)
# print(family1.is_18('Itay'))
#
# family1.member_printer()