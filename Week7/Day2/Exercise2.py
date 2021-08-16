import random


def get_random_temp(season):
    if season == "winter":
        return round(random.uniform(-10, 16), 2)
    elif season == "fall":
        return round(random.uniform(16, 23), 2)
    elif season == "spring":
        return round(random.uniform(23, 32), 2)
    elif season == "summer":
        return round(random.uniform(32, 40), 2)
    else:
        return round(random.uniform(65, 111), 2)



def main():
    user_season = input("Choose a season.\n")
    temp = get_random_temp(user_season)
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif temp > 0 and temp < 16:
        print("Quite cold! Don’t forget your coat")
    elif temp > 16 and temp < 23:
        print("It's chilly out side.")
    elif temp > 23 and temp < 32:
        print("It's a nice day!")
    elif temp > 32 and temp < 40:
        print("It's hot outside")
    else:
        print("What?")
main()

