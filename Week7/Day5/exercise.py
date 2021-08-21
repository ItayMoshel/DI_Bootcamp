some_list = ['a', 'b', 'c', 'b', 'd', 'e', 'f', 'f', 'a', 'c', 'd', 'e']

repeating_letter = 0
list_of_repeating_letters = []
for i in some_list:
    if some_list.count(i) > 1:
        repeating_letter += 1
        if i not in list_of_repeating_letters:
            list_of_repeating_letters.append(i)


print(repeating_letter, list_of_repeating_letters)


picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

def picture_display():
    for i in picture:
        picture_list = []
        for n in i:
            if n == 0:
                picture_list.append(" ")
            if n == 1:
                picture_list.append("*")
        print(*picture_list)

picture_display()

#selution
for i in picture:
    for n in i:
        if n == 0:
            print(" ", end="")
        if n == 1:
            print("*", end="")
    print("")


