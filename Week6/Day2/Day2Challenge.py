import random

user_input = input("please insert 10 character string.\n")
user_input_length = len(user_input)

if user_input_length > 10:
    print("string too long")
elif user_input_length < 10:
    print("string not long enough")
else:
    print(f"the first letter of your string is {user_input[0]}, and the last letter is {user_input[9]}")

print(f'''
{user_input[0]}
{user_input[0]}{user_input[1]}
{user_input[0]}{user_input[1]}{user_input[2]}
{user_input[0]}{user_input[1]}{user_input[2]}{user_input[3]}
{user_input[0]}{user_input[1]}{user_input[2]}{user_input[3]}{user_input[4]}
{user_input[0]}{user_input[1]}{user_input[2]}{user_input[3]}{user_input[4]}{user_input[5]}
{user_input[0]}{user_input[1]}{user_input[2]}{user_input[3]}{user_input[4]}{user_input[5]}{user_input[6]}
{user_input[0]}{user_input[1]}{user_input[2]}{user_input[3]}{user_input[4]}{user_input[5]}{user_input[6]}{user_input[7]}
{user_input[0]}{user_input[1]}{user_input[2]}{user_input[3]}{user_input[4]}{user_input[5]}{user_input[6]}{user_input[7]}{user_input[8]}
{user_input[0]}{user_input[1]}{user_input[2]}{user_input[3]}{user_input[4]}{user_input[5]}{user_input[6]}{user_input[7]}{user_input[8]}{user_input[9]}
''')

# is there any way of doing this ^^^^ with a for loop?

input_list = list(user_input)
random.shuffle(input_list)
input_shuffle = ''.join(input_list)
print(input_shuffle)

