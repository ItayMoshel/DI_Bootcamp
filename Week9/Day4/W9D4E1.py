class Human:

    def __init__(self, name=str, age=int, living_place=None):
        self.name = name
        self.age = age
        self.living_place = living_place

    def move(self, building):
        self.living_place = building



class Building:

    def __init__(self, address, inhabitants):
        self.address = address
        self.inhabitants = inhabitants


class City:

    def __init__(self, name=str, buildings=list):
        self.name = name
        self.buildings = buildings


