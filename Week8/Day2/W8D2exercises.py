# Exercise XP:
# Exercise1: Cats
# cat_dict = {}
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def add_cat_To_dict(self):
#         cat_dict[self.name] = self.age
#
#
# cat1 = Cat('mittens', 12)
# cat2 = Cat('roger', 13)
# cat3 = Cat('norman', 21)
# cat1.add_cat_To_dict()
# cat2.add_cat_To_dict()
# cat3.add_cat_To_dict()
#
# def oldest_cat():
# max = 0
# for key, value in cat_dict.items():
#     if value > max:
#         max = value
#         if max > : can't find a way to implement this method.
#             print(f"The oldest cat is {key}, and he is {value} years old.")

# oldest_cat()

# Exercise 2: Dogs

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


davids_dog = Dog("Rex", 50)
print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.height > davids_dog.height:
    print(sarahs_dog.name)
else:
    print(davids_dog.name)


# Exercise 3: Song

class Song():
    def __init__(self, lyrics):
        self.lyrics = list(lyrics)

    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)


stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
tnt = Song(["I'm dirty, mean and mighty unclean", "I'm a wanted man", "Public enemy number one", "Understand?"])
stairway.sing_me_a_song()
tnt.sing_me_a_song()


# Exercise 4: Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animal(self):
        print(*self.animals)

    def sell_animal(self, animal_sold):
        self.animals.remove(animal_sold)

    def sort_animals(self):
        animal_dict = {}
        self.animals.sort()
        for key in range(1, len(self.animals)):
            for animal in self.animals:
                animal_dict[key] = self.animals[key]
        print(animal_dict)


ramat_gan_safari = Zoo("Ramat gan safari")

ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Owl")

ramat_gan_safari.get_animal()
ramat_gan_safari.sell_animal("Eel")
ramat_gan_safari.get_animal()
ramat_gan_safari.sort_animals()

# dict = {}
#
# lst = ["a", "b", "c", "d", "e", "f", "g"]
#
#
# for key in range(1, len(lst)):
#     for i in lst:
#         dict[key] = list[i]
# print(dict)
