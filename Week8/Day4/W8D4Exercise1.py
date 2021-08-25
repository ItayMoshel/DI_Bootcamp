class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Persian(Cat):
    pass


cat1 = Bengal("cat1", 10)
cat2 = Chartreux("cat2", 20)
cat3 = Persian("cat3", 30)

cat_list = [cat1, cat2, cat3]

my_pets = cat_list[0]  # (?)

for cat in cat_list:
    print(cat.walk())  # Don't think i got the instruction right.


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        strenght = self.run_speed() * self.weight
        other_dog_strenght = other_dog.run_speed() * other_dog.weight
        if strenght > other_dog_strenght:
            return f"{self.name} is won the fight."
        else:
            return f"{other_dog.name} won the fight."


dog1 = Dog("Bob", 10, 12)
dog2 = Dog("Obo", 12, 14)
dog3 = Dog("Oob", 14, 16)

print(dog1.fight(dog3))
