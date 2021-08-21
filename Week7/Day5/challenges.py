# Daily Challenge is at the bottom of the file.


# Write a script that inserts an item at a defined index in a list.

# def list_insert(name_of_list, index, item):
#     name_of_list[index] += " " + item
#     item_split = name_of_list[index].split(" ")
#     new_item = list(item_split)
#     newlist[index] = new_item[-1]
#     newlist.append(new_item[0])
#
#
#
# newlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
# print(newlist)
# list_insert(newlist, 11, "apple")
# print(newlist)

# def list_insert(list_name, index, item):
#     list_name.insert(index, item)
#
# listnew = ['zero', 'one', 'two']
#
# print(listnew)
# list_insert(listnew, 1, "between zero and one")
# print(listnew)




# Write a script that counts the number of spaces in a string.

def space_count(string):
    num_of_spaces = 0
    for i in string:
        if i == " ":
            num_of_spaces += 1
    return num_of_spaces

print(space_count("Write a script that counts the number of spaces in a string."))




# Write a script that calculates the number of upper case letters and lower case letters in a string.

def case_letters(string):
    num_of_lowcase = 0
    num_of_upcase = 0
    for i in string:
        if i.isupper():
            num_of_upcase += 1
        if i.islower():
            num_of_lowcase += 1
    return (f"number of lower: {num_of_lowcase}, number of upper: {num_of_upcase}")

string = "Is ThAt RiGhT"
print(case_letters(string))




# Write a function to find the sum of an array without using the built in function:

def array_sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(array_sum(list_of_numbers))




# Write a function to find the max number in a list

def find_max_num(list):
    max = 0
    for number in list:
        if number > max:
            max = number
    print(max)


list_of_num = [0, 1, 3, 50, 49, 82, 81]
find_max_num(list_of_num)




# Write a function that returns factorial of a number

def factorial(number):
    fac = 1
    for i in range(1, number +1):
        fac = fac * i
    return fac

print(factorial(4))




image1 = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1]
]

image2 = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

image3 = [
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1]
]
def image_printer(image):
    for i in image:
        for n in i:
            if n == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print(" ")

image_printer(image1)
image_printer(image2)
image_printer(image3)


# Daily Challenge

def sorted_list():
    input_to_sort = input("write words separated bt comma:\n")
    separated_input = input_to_sort.split(",")
    new_list = [x for x in separated_input]
    new_list.sort()
    print(','.join(new_list))

sorted_list()