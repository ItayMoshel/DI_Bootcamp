import math

my_fav_numbers = set()
my_fav_numbers.add(7)
my_fav_numbers.add(5)
my_fav_numbers.remove(5)
print(my_fav_numbers)

friend_fav_numbers = set()
friend_fav_numbers.add(65)
friend_fav_numbers.add(56)
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# you can't add items to a tuple, tuple is unchangeable.
list_of_numbers = (1, 2, 3, 4, 5)
print(list_of_numbers)
# we can change it to list, and add to the list.
list10 = list(list_of_numbers)
list10.append(1)
# then change back to tuple.
list2_of_numbers = tuple(list10)
print(list2_of_numbers)

for i in range(1, 21):
    print(i)

# integer is a whole number without a decimal point.
# float is a number with decimal point.

# didn't understood the instructions.


basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.pop(2)  # / .pop(-1)
basket.append("Kiwi")
basket.insert(0, "Apples")
num_of_apples = basket.count("Apples")
basket.clear()

print(basket)

basket2 = ["Banana", "Apples", "Oranges", "Blueberries", "Kiwi", "Watermelon"]

for i in range(0, len(basket2)):
    if i % 2 == 0:
        print(basket2[i])

number1 = 1500
number2 = 2500

for i in range(number1, number2 + 1):
    if i % 5 == 0 and i % 7 == 0:
        print(i)

users_fav_fruit = input("What is your favorite fruit/s?\n")
list_of_users_fruits = users_fav_fruit.split(" ")
users_answer = input(("Please name a fruit.\n"))

if users_answer in list_of_users_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
elif users_answer not in list_of_numbers:
    print("You chose a new fruit. I hope you enjoy")

    #########################################
    # XP GOLD

list_one = [1, 2, 3, 4, 5]
list_two = [6, 7, 8, 9, 10]

list_one.extend(list_two)
print(list_one)

highest_number = 0
for i in range(1, 4):
    user_input = input("input a number")
    input_as_int = int(user_input)
    if input_as_int > highest_number:
        highest_number = input_as_int
print(highest_number)

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("what is your name?")

if user_name in names:
    print(names.index(user_name))

##########################################
# Ninja exercise.


c = 50
h = 30
d = input("insert numbers separated with commas.\n")

d_list = d.split(",")

for number in d_list:
    number_as_int = int(number)
    d = number_as_int
    q = math.sqrt((2 * c * d) / h)
print(round(q))

list_of_numbers = [18, 19, 2, 56, 33, 17, 41, 33, 1, 1]

for i in list_of_numbers:
    print(i, end=" ")

sorted = sorted(list_of_numbers, reverse=True)
print(sorted)

sum_of_all = sum(list_of_numbers)
print(sum_of_all)

new_list = [list_of_numbers[0], list_of_numbers[-1]]
print(new_list)

above_50 = []
for number in list_of_numbers:
    if number > 50:
        above_50.append(number)

print(above_50)

below_10 = []
for number in list_of_numbers:
    if number < 10:
        below_10.append(number)

print(below_10)

sqrt_list = []
for number in list_of_numbers:
    sqrt_list.append(number ** 2)

print(sqrt_list)

list_as_set = set(list_of_numbers)
print(list_as_set)

average_list = sum_of_all / 10
print(average_list)

largest_number = max(list_of_numbers)
print(largest_number)

smallest_number = min(list_of_numbers)
print(smallest_number)

user_number = []
for number in range(11):
    number = input("insert number from -100 to 100\n")
    number_as_int = int(number)
    user_number.append(number_as_int)

print(user_number)
