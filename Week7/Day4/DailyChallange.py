def false_function(number):
    try:
        print(number / 0)
    except ZeroDivisionError:
        print("Can't divide by 0")

false_function(5)