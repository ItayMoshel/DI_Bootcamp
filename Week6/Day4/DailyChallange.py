from datetime import datetime

current_date = datetime.today().strftime('%Y-%m-%d')
list_date = current_date.split("-")
year_as_int = int(list_date[0])


user_bday = input("When you were born? please use this pattern ---> YYYY/MM/DD.\n")
bday_list = user_bday.split("/")
user_year_as_int = int(bday_list[0])


user_age = year_as_int - user_year_as_int
user_age_as_str = str(user_age)
last_age_number = int(user_age_as_str[-1])

if user_year_as_int % 4 == 0:
    if user_year_as_int % 100 == 0:
        if user_year_as_int % 400 == 0:
            print("   ___" + "i" * last_age_number + "___   " + "           ___" + "i" * last_age_number + "___")
            print("   |:H:a:p:p:y:|      " + "  |:H:a:p:p:y:|   ")
            print(" __|___________|__   " + " __|___________|__")
            print("|^^^^^^^^^^^^^^^^^|   " + "|^^^^^^^^^^^^^^^^^|")
            print("|:B:i:r:t:h:d:a:y:|   " + "|:B:i:r:t:h:d:a:y:|")
            print("|                 |   " + "|                 |")
            print("~~~~~~~~~~~~~~~~~~~   " + "~~~~~~~~~~~~~~~~~~~")
else:
    print("   ___" + "i" * last_age_number + "___")
    print("   |:H:a:p:p:y:|   ")
    print(" __|___________|__")
    print("|^^^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")
