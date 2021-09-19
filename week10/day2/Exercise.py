import random


# Exercise ONE
def display_message():
    print("Now learning PYTHON.")


# display_message()


# Exercise TWO
def fav_book(title):
    print(f"One of my favorite books is {title}")


# fav_book("Think of a number")


# Exercise THREE
def describe_city(city, country="israel"):
    print(f"{city} is in {country}")


# describe_city("tel aviv")


# Exercise FOUR
def random_number(number):
    random_num = random.randint(1, 100)
    print(random_num)
    if number == random_num:
        print("Success!")
    else:
        print(f"Failure.\nThe number you choose: {number},\nThe number the computer choose: {random_num}.")

#
# random_number(45)


# Exercise FIVE
def make_shirt(size="L", message="I Love Python"):
    print(f'The message is "{message}", and the size is {size}.')

#
# make_shirt("M", "Hello")
# make_shirt("L")
# make_shirt("M")
# make_shirt("S", "Why so serious?")
# make_shirt(message="Nothing to see here", size="XXL")

# Exercise SIX
magicians_names = ["David Copperfield", "Doug Henning", "Siegfried and Roy", "Lance Burton", "Ricky Jay"]


def show_magicians():
    for magician in magicians_names:
        print(magician)


# show_magicians()


def make_great():
    for i in range(0, len(magicians_names)):
        magicians_names[i] += " the great"


# make_great()
# show_magicians()
