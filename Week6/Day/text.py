my_age = 27
my_future_age = my_age + 123879
print(my_future_age)

first_name = "itay"
last_name = "moshel"
print(first_name + " " + last_name)

age = input("How old are you? ") #input will be string
print("You are {} years old".format(age)) #will outpot the age input as a string

number = int(input("please enter a number between 1-100:\n"))
if number%3==0:
	print('Fizz', end='')
if number%5==0:
    
	print('Buzz')