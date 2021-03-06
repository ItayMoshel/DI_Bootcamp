from typing import List


class Human:

    def __init__(self, name, age, living_place):
        self.name = name
        self.age = age
        self.living_place = living_place

    def move(self, building):
        self.living_place = building
        building.inhabitants.append(self)


class Building:

    def __init__(self, address, inhabitants: List = None):
        self.address = address
        if not inhabitants:
            inhabitants = []

        self.inhabitants = inhabitants


class City:

    def __init__(self, name, buildings):
        self.name = name
        self.buildings = buildings

    def construct(self, address):
        new_building = Building(address)
        self.buildings.append(new_building)

    def info(self, address):
        print(f"the number if buildings is {self.buildings}")
        total_ages = 0
        total_citizens = 0

        for building in self.buildings:
            total_citizens += len(building.inhabitants)

            for human in building.inhabitants:
                total_ages += human.age

        print(f"the mean age is {total_ages / total_citizens}")
