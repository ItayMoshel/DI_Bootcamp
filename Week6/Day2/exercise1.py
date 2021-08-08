print("Hello world\n"*4)

print((99^3)*8)

# 5 < 3 => False
# 3 == 3 => True
# 3 == '3' => False
# "Hello" == "hello" => False (?)

print(5 < 3, 3 == 3, 3 == '3', "Hello" == "hello")

computer_brand = "apple"
print(f"I have a {computer_brand} computer")

name = "itay"
age = 27
shoe_size = 39
info = f"my name is {name}, i am {age} years old and my shoe size is {shoe_size}."
print(info)

a = 10
b = 5

if a > b:
    print("Hello world")


user_input = int(input("please choose a number.\n"))

if user_input % 2 == 0:
    print(f"The number you choose is a even number: {user_input}")
else:
    print(f"The number you choose is a odd number: {user_input}")


my_name = "itay"
users_name = input("what is your first name?\n")

if my_name == users_name:
    print("CAN'T BELIEVE IT. WE HAVE THE SAME NAME")
else:
    print("I guess my name is prettier.")


users_height = int(input("what is your height in inch?\n"))
users_height_conv = users_height * 2.54
min_height = 145

if users_height_conv > min_height:
    print("You are tall enough to ride the roller coaster, enjoy!")
elif users_height_conv < min_height:
    print("You are NOT tall enough to ride the roller coaster, grow some more and come back when you are taller.")
