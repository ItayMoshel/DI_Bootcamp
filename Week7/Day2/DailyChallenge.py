matrix = [
    ['7', 'i', '3'],
    ['T', 's', 'i'],
    ['h', '%', 'x'],
    ['i', ' ', '#'],
    ['s', 'm', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

decoded_matrix = ""

# for loop to iterate over the columns
for i in range(len(matrix[0])):
    # for loop to iterate over the rows
    for n in range(len(matrix)):
        letter = matrix[n][i]
        if letter.isalpha():
            decoded_matrix += letter
        else:
            if decoded_matrix:
                if decoded_matrix[-1] != " ":
                    decoded_matrix += " "

print(decoded_matrix)