class Character:

    def __init__(self, name, life: int = 20, attack: int = 10):
        self.name = name
        self.life = life
        self.attack = attack

        print(f"hey! my name is{self.name}.")

    def basic_attack(self, opponent):
        opponent.life -= self.attack


class Druid(Character):

    def meditate(self):
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        self.attack += 5

    def fight(self, opponent):
        opponent.life -= (0.75 * self.life + 0.75 * self.attack)


class Warrior(Character):

    def brawl(self, opponent):
        opponent.life -= (2 * self.attack)
        self.life += (0.5 * self.attack)

    def train(self):
        self.life += 2
        self.attack += 2

    def roar(self, opponent):
        opponent.attack -= 3


class Mage(Character):

    def curse(self, opponent):
        opponent.attack -= 2

    def summon(self):
        self.attack += 3

    def cast_spell(self, opponent):
        opponent.life -= self.attack / self.life


war = Warrior('Jack', 100, 20)
mage = Mage('Norm', 100, 15)
druid = Druid('Vic', 100, 14)

print(war.attack)
mage.curse(war)
print(war.attack)

print(mage.life)
war.basic_attack(mage)
print(mage.life)

print(war.life)
druid.fight(war)
print(war.life)

for i in range(10):
    war.train()
print(war.life, war.attack)

print(mage.attack)
for i in range(10):
    mage.summon()
print(mage.attack)

print(druid.life)
for i in range(10):
    druid.meditate()
print(druid.life)
