import random

from W8D4Exercise1 import Dog


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        Dog.__init__(self, name, age, weight) # / super().__init__(name, age, weight) <--- ?
        self.trained = trained

    def trained1(self):
        self.trained = True
        self.bark()

    def play(self, *args):
        print(f"{args}, all play together")

    def do_a_trick(self):
        if self.trained:
            list_of_tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {list_of_tricks[random.randint(0, len(list_of_tricks) - 1)]}")


pet1 = PetDog("Bobie", 9, 12)
pet1.play("a", "b", "c", "d")
pet1.trained1()
pet1.do_a_trick()
