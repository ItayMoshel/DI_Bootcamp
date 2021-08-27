# import random
#
#
# class Game:
#     def __init__(self, user_item, computer_item):
#         self.user_item = user_item
#         self.computer_item = computer_item
#
#     def get_user_item(self):
#         global user_input
#         while True:
#             self.user_item = user_input
#             try:
#                 user_input = int(input("Please select an item: 1.Rock 2.Paper 3.Scissors"))
#                 return user_input
#             except ValueError:
#                 # print("Please select an item: 1.Rock 2.Paper 3.Scissors")
#                 continue
#
#     def get_computer_item(self):
#         rock = 1
#         paper = 2
#         scissors = 3
#         list_of_choice = [rock, paper, scissors]
#         return list_of_choice[random.randint(0, 2)]
#
#     def get_game_result(self, user_item, computer_item):
#         self.user_item = user_item
#         self.computer_item = computer_item
#         if user_item == 3 and computer_item == 1:
#             return "Lose"
#         if user_item == 1 and computer_item ==3:
#             return "Win"
#         if computer_item > user_item:
#             return "Lose"
#         if user_item > computer_item:
#             return "Win"
#         if user_item == computer_item:
#             return "Draw"
#
#     def play(self):
#         user_item = self.get_user_item()
#         computer_item = self.get_computer_item()
#


import random


class Game:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __init__(self, user_item, computer_item):
        self.user_item = user_item
        self.computer_item = computer_item

    def get_user_item(self):
        global user_input
        while True:
            self.user_item = user_input
            try:
                user_input = int(input("Please select an item: 1.Rock 2.Paper 3.Scissors"))
                return user_input
            except ValueError:
                # print("Please select an item: 1.Rock 2.Paper 3.Scissors")
                continue

    def get_computer_item(self):
        list_of_choice = [Game.ROCK, Game.PAPER, Game.SCISSORS]
        return list_of_choice[random.randint(0, 2)]

    def get_game_result(self, user_item, computer_item):
        self.user_item = user_item
        self.computer_item = computer_item
        if user_item == Game.SCISSORS and computer_item == Game.ROCK:
            return "You Lose"
        if user_item == Game.ROCK and computer_item == Game.SCISSORS:
            return "You Win"
        if computer_item > user_item:
            return "You Lose"
        if user_item > computer_item:
            return "You Win"
        if user_item == computer_item:
            return "Draw"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        game_result = self.get_game_result()
        print(f"you selected {user_item}. the computer selected {computer_item}. {game_result}")
        self.get_game_result()