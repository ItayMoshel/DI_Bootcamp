import random


class Card:
    hearts = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    clubs = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    spades = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    diamonds = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suit_list = ["hearts", "clubs", "spades", "diamonds"]
    deck = 52

    def __init__(self):
        self.list = [self.hearts, self.clubs, self.spades, self.diamonds]


class Deck(Card):

    def shuffle(self):
        self.deck = 52
        for i in self.list:
            random.shuffle(self.list)

    def deal(self):
        print(self.list[random.randrange(0, len(self.list) - 1)][random.randrange(0, 13)], random.choice(self.suit_list))
        self.deck -= 1

card = Deck()

print(card.deck)
print(card.deal()) # why the None ?
print(card.deck)
print(card.deal())
print(card.deck)
card.shuffle()
print(card.deck)
print(card.deal())
print(card.deck)

# tried to do it with dict
# cards = {
#     "diamonds": ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
#     "spades": ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
#     "clubs": ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
#     "hearts": ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# }
#
# storage = random.choice(list(cards.values()))
# print(storage[random.randrange(0, 13)])
#
#
# # for key, value in cards.items():
# #     random.shuffle(cards[key][value])
# #     print(key, value)
#
# print(cards)
# random.shuffle(cards)