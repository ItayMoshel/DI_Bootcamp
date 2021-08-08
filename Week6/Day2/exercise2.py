print("Hello world\n"*4 + "I love python\n"*4)

user_input = int(input("Please choose a month from 1 to 12.\n"))

if user_input <= 5 and user_input >= 3:
    print("Spring")
elif user_input <= 8 and user_input >= 6:
    print("Summer")
elif user_input <= 11 and user_input >= 9:
    print("Autumn")
elif user_input == 12 or user_input <= 2: #  <==== is this the best way to write it?
    print("Winter")


    


