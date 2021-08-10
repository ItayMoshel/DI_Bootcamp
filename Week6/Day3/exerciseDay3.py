

user_input = int(input("Please insert a number\n"))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number * user_input)


que = input("Yes or no?")

while que == "yes":
    que = input("yes or no?")
else:
    print("ok")


current_number = 1

while current_number <= 10:
    print(current_number)
    current_number += 1

for i in range(1, 11):
    print(i)


all_names = []

name = input("enter a name. after, enter 'done'\n")

while name != 'done':
    all_names.append(name)
    name = input("enter a name. after, enter 'done'\n")



print(all_names)