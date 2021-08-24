class Farm():
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animal_dictionary = {}

    def add_animal(self, animal_type = 'str', num_of_animal=1):
        self.animal_dictionary[animal_type] = num_of_animal
        return num_of_animal


    def get_info(self):
        print(self.farm_name + "'s farm")
        print(self.animal_dictionary)



mcdonald = Farm("McDonald")
mcdonald.add_animal('goat', 12)
mcdonald.add_animal('sheep', 1)
mcdonald.add_animal('sheep', 1)
mcdonald.add_animal('cow', 5)
print(mcdonald.get_info())